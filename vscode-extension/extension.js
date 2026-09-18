const vscode = require('vscode');

/**
 * Activates the AiraLang extension
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    const runFileDisposable = vscode.commands.registerCommand('airalang.runFile', async (fileUri) => {
        let filePath = '';

        if (fileUri && fileUri.fsPath) {
            filePath = fileUri.fsPath;
        } else {
            const editor = vscode.window.activeTextEditor;
            if (editor && editor.document) {
                if (editor.document.isDirty) {
                    await editor.document.save();
                }
                filePath = editor.document.fileName;
            }
        }

        if (!filePath) {
            vscode.window.showWarningMessage('No active AiraLang (.aira) file to run.');
            return;
        }

        // Reuse existing AiraLang terminal or create a new one
        let terminal = vscode.window.terminals.find((t) => t.name === 'AiraLang');
        if (!terminal) {
            terminal = vscode.window.createTerminal('AiraLang');
        }

        terminal.show(true);
        terminal.sendText(`airalang "${filePath}"`);
    });

    context.subscriptions.push(runFileDisposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
