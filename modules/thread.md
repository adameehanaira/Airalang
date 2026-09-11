# 🧵 AiraLang `thread` Module
> **Concurrency, Worker Pools & Multithreading**

## Import
```aira
import "thread";
```

## Methods
- `thread.spawn(fn, [args])`: Launch function in background thread.
- `thread.join(thread_handle, [timeout])`: Wait for thread completion.
- `thread.sleep(seconds)`: Thread sleep delay.
- `thread.pool(fn, items, [max_workers=5])`: Parallel execution over collection.

## Example
```aira
import "thread";

fn task(id) {
    return "Task " + id + " done";
}

let res = thread.pool(task, [1, 2, 3, 4], 4);
say res;
```
