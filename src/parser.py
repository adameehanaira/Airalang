from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def peek(self, offset=1):
        if self.pos + offset < len(self.tokens):
            return self.tokens[self.pos + offset]
        return self.tokens[-1]

    def match(self, *types):
        if self.current().type in types:
            tok = self.current()
            self.pos += 1
            return tok
        return None

    def expect(self, type_):
        tok = self.match(type_)
        if not tok:
            curr = self.current()
            raise SyntaxError(f"AiraLang SyntaxError: Expected '{type_}' but got '{curr.type}' ({repr(curr.value)}) at line {curr.line}, col {curr.col}")
        return tok

    def parse(self):
        statements = []
        while self.current().type != "EOF":
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return ProgramNode(statements)

    def parse_statement(self):
        tok = self.current()

        if self.match("SEMICOLON"):
            return None

        # standalone block statement: `{ stmt1; stmt2; }`
        if tok.type == "LBRACE":
            return self.parse_block_or_statement()

        # import / load / use statement: `import os;`, `import "math";`
        if tok.type in ("IMPORT", "LOAD", "USE"):
            self.pos += 1
            if self.current().type in ("STRING", "IDENTIFIER"):
                mod_tok = self.current()
                self.pos += 1
            else:
                curr = self.current()
                raise SyntaxError(f"AiraLang SyntaxError: Expected module name or string after '{tok.value}' at line {curr.line}, col {curr.col}")
            self.match("SEMICOLON")
            return ImportStatementNode(str(mod_tok.value), tok.line)

        # say / print statement: `say "A", "B", 10;`
        if tok.type in ("SAY", "PRINT"):
            self.pos += 1
            expressions = [self.parse_expression()]
            while self.match("COMMA"):
                expressions.append(self.parse_expression())
            self.match("SEMICOLON")
            return SayStatementNode(expressions, tok.line)

        # let statement: `let name = expr;`
        if tok.type == "LET":
            self.pos += 1
            name_tok = self.expect("IDENTIFIER")
            self.expect("ASSIGN")
            expr = self.parse_expression()
            self.match("SEMICOLON")
            return LetStatementNode(name_tok.value, expr, tok.line)

        # if statement: `if (cond) { ... } else { ... }`
        if tok.type == "IF":
            self.pos += 1
            has_paren = self.match("LPAREN")
            cond = self.parse_expression()
            if has_paren:
                self.expect("RPAREN")
            then_branch = self.parse_block_or_statement()
            else_branch = None
            if self.match("ELSE"):
                else_branch = self.parse_block_or_statement()
            return IfStatementNode(cond, then_branch, else_branch, tok.line)

        # while statement: `while (cond) { ... }`
        if tok.type == "WHILE":
            self.pos += 1
            has_paren = self.match("LPAREN")
            cond = self.parse_expression()
            if has_paren:
                self.expect("RPAREN")
            body = self.parse_block_or_statement()
            return WhileStatementNode(cond, body, tok.line)

        # for statement: `for item in items { ... }` or `for (item in items) { ... }` or `for (let item in items) { ... }`
        if tok.type == "FOR":
            self.pos += 1
            has_paren = self.match("LPAREN")
            self.match("LET") # optional let
            var_tok = self.expect("IDENTIFIER")
            self.expect("IN")
            iterable = self.parse_expression()
            if has_paren:
                self.expect("RPAREN")
            body = self.parse_block_or_statement()
            return ForInStatementNode(var_tok.value, iterable, body, tok.line)

        # try / catch statement: `try { ... } catch (err) { ... }`
        if tok.type == "TRY":
            self.pos += 1
            try_body = self.parse_block_or_statement()
            self.expect("CATCH")
            has_paren = self.match("LPAREN")
            err_var = "error"
            if self.current().type == "IDENTIFIER":
                err_var = self.expect("IDENTIFIER").value
            if has_paren:
                self.expect("RPAREN")
            catch_body = self.parse_block_or_statement()
            return TryCatchStatementNode(try_body, err_var, catch_body, tok.line)

        # throw statement: `throw "Error description";`
        if tok.type == "THROW":
            self.pos += 1
            expr = self.parse_expression()
            self.match("SEMICOLON")
            return ThrowStatementNode(expr, tok.line)

        # break statement: `break;`
        if tok.type == "BREAK":
            self.pos += 1
            self.match("SEMICOLON")
            return BreakStatementNode(tok.line)

        # continue statement: `continue;`
        if tok.type == "CONTINUE":
            self.pos += 1
            self.match("SEMICOLON")
            return ContinueStatementNode(tok.line)

        # fn statement: `fn name(a, b) { ... }`
        if tok.type == "FN":
            self.pos += 1
            name_tok = self.expect("IDENTIFIER")
            self.expect("LPAREN")
            params = []
            if self.current().type != "RPAREN":
                params.append(self.expect("IDENTIFIER").value)
                while self.match("COMMA"):
                    params.append(self.expect("IDENTIFIER").value)
            self.expect("RPAREN")
            body = self.parse_block_or_statement()
            return FunctionDefNode(name_tok.value, params, body, tok.line)

        # class statement: `class Person { fn init(name) { ... } fn greet() { ... } }`
        if tok.type == "CLASS":
            self.pos += 1
            name_tok = self.expect("IDENTIFIER")
            self.expect("LBRACE")
            methods = {}
            while self.current().type != "RBRACE" and self.current().type != "EOF":
                if self.match("FN") or self.current().type == "IDENTIFIER":
                    # allow either `fn name()` or `name()`
                    if self.tokens[self.pos - 1].type != "FN":
                        m_name_tok = self.expect("IDENTIFIER")
                    else:
                        m_name_tok = self.expect("IDENTIFIER")
                    self.expect("LPAREN")
                    m_params = []
                    if self.current().type != "RPAREN":
                        m_params.append(self.expect("IDENTIFIER").value)
                        while self.match("COMMA"):
                            m_params.append(self.expect("IDENTIFIER").value)
                    self.expect("RPAREN")
                    m_body = self.parse_block_or_statement()
                    methods[m_name_tok.value] = FunctionDefNode(m_name_tok.value, m_params, m_body, m_name_tok.line)
                elif self.match("SEMICOLON"):
                    pass
                else:
                    curr = self.current()
                    raise SyntaxError(f"AiraLang SyntaxError: Expected method in class '{name_tok.value}' at line {curr.line}")
            self.expect("RBRACE")
            return ClassDefNode(name_tok.value, methods, tok.line)

        # return statement: `return expr;`
        if tok.type == "RETURN":
            self.pos += 1
            expr = None
            if self.current().type not in ("SEMICOLON", "RBRACE", "EOF"):
                expr = self.parse_expression()
            self.match("SEMICOLON")
            return ReturnStatementNode(expr, tok.line)

        # expression / assignment statement
        expr = self.parse_expression()
        if self.match("ASSIGN"):
            val_expr = self.parse_expression()
            self.match("SEMICOLON")
            if isinstance(expr, IdentifierNode):
                return AssignStatementNode(expr.name, val_expr, tok.line)
            elif isinstance(expr, IndexAccessNode):
                return IndexAssignStatementNode(expr.target, expr.index, val_expr, tok.line)
            elif isinstance(expr, MemberAccessNode):
                return MemberAssignStatementNode(expr.target, expr.member, val_expr, tok.line)
            else:
                raise SyntaxError(f"AiraLang SyntaxError: Invalid assignment target at line {tok.line}")

        self.match("SEMICOLON")
        return ExpressionStatementNode(expr)

    def parse_block_or_statement(self):
        if self.match("LBRACE"):
            stmts = []
            while self.current().type not in ("RBRACE", "EOF"):
                s = self.parse_statement()
                if s:
                    stmts.append(s)
            self.expect("RBRACE")
            return BlockNode(stmts)
        else:
            return self.parse_statement()

    # Expressions
    def parse_expression(self):
        return self.parse_logical_or()

    def parse_logical_or(self):
        left = self.parse_logical_and()
        while self.current().type == "OR":
            op = self.current()
            self.pos += 1
            right = self.parse_logical_and()
            left = BinaryOpNode(left, "or", right, op.line)
        return left

    def parse_logical_and(self):
        left = self.parse_equality()
        while self.current().type == "AND":
            op = self.current()
            self.pos += 1
            right = self.parse_equality()
            left = BinaryOpNode(left, "and", right, op.line)
        return left

    def parse_equality(self):
        left = self.parse_relational()
        while self.current().type in ("EQ_EQ", "NOT_EQ"):
            op = self.current()
            self.pos += 1
            right = self.parse_relational()
            left = BinaryOpNode(left, op.value, right, op.line)
        return left

    def parse_relational(self):
        left = self.parse_additive()
        while self.current().type in ("LT", "GT", "LTE", "GTE"):
            op = self.current()
            self.pos += 1
            right = self.parse_additive()
            left = BinaryOpNode(left, op.value, right, op.line)
        return left

    def parse_additive(self):
        left = self.parse_multiplicative()
        while self.current().type in ("PLUS", "MINUS"):
            op = self.current()
            self.pos += 1
            right = self.parse_multiplicative()
            left = BinaryOpNode(left, op.value, right, op.line)
        return left

    def parse_multiplicative(self):
        left = self.parse_unary()
        while self.current().type in ("MUL", "DIV", "MOD"):
            op = self.current()
            self.pos += 1
            right = self.parse_unary()
            left = BinaryOpNode(left, op.value, right, op.line)
        return left

    def parse_unary(self):
        if self.current().type in ("MINUS", "NOT"):
            op = self.current()
            self.pos += 1
            right = self.parse_unary()
            return UnaryOpNode(op.value, right, op.line)
        return self.parse_postfix()

    def parse_postfix(self):
        atom = self.parse_atom()
        while True:
            if self.match("LPAREN"):
                args = []
                if self.current().type != "RPAREN":
                    args.append(self.parse_expression())
                    while self.match("COMMA"):
                        args.append(self.parse_expression())
                self.expect("RPAREN")
                atom = FunctionCallNode(atom, args, getattr(atom, 'line', self.current().line))
            elif self.match("DOT"):
                member_tok = self.expect("IDENTIFIER")
                atom = MemberAccessNode(atom, member_tok.value, member_tok.line)
            elif self.match("LBRACKET"):
                idx_expr = self.parse_expression()
                self.expect("RBRACKET")
                atom = IndexAccessNode(atom, idx_expr, getattr(atom, 'line', self.current().line))
            else:
                break
        return atom

    def parse_atom(self):
        tok = self.current()
        if self.match("NUMBER"):
            return LiteralNode(tok.value, "NUMBER", tok.line)
        if self.match("STRING"):
            return LiteralNode(tok.value, "STRING", tok.line)
        if self.match("TRUE"):
            return LiteralNode(True, "BOOLEAN", tok.line)
        if self.match("FALSE"):
            return LiteralNode(False, "BOOLEAN", tok.line)
        if self.match("NULL"):
            return LiteralNode(None, "NULL", tok.line)
        if self.match("THIS"):
            return ThisNode(tok.line)
        if self.match("NEW"):
            class_tok = self.expect("IDENTIFIER")
            args = []
            if self.match("LPAREN"):
                if self.current().type != "RPAREN":
                    args.append(self.parse_expression())
                    while self.match("COMMA"):
                        args.append(self.parse_expression())
                self.expect("RPAREN")
            return NewInstanceNode(class_tok.value, args, tok.line)
        if self.match("IDENTIFIER"):
            return IdentifierNode(tok.value, tok.line)
        if self.match("LPAREN"):
            expr = self.parse_expression()
            self.expect("RPAREN")
            return expr
        if self.match("LBRACKET"):
            elements = []
            if self.current().type != "RBRACKET":
                elements.append(self.parse_expression())
                while self.match("COMMA"):
                    elements.append(self.parse_expression())
            self.expect("RBRACKET")
            return ListNode(elements, tok.line)
        if self.match("LBRACE"):
            pairs = []
            if self.current().type != "RBRACE":
                key_expr = self.parse_expression()
                self.expect("COLON")
                val_expr = self.parse_expression()
                pairs.append((key_expr, val_expr))
                while self.match("COMMA"):
                    if self.current().type == "RBRACE":
                        break
                    k = self.parse_expression()
                    self.expect("COLON")
                    v = self.parse_expression()
                    pairs.append((k, v))
            self.expect("RBRACE")
            return DictNode(pairs, tok.line)

        raise SyntaxError(f"AiraLang SyntaxError: Unexpected token '{tok.type}' ({repr(tok.value)}) at line {tok.line}, col {tok.col}")
