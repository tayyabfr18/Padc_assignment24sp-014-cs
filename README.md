# 🚀 PADC Assignment - Chapter 2: Python Parallel Programming Cookbook

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 👤 Student Information
* **Name:** Muhammad Tayyab
* **Student ID:** `24SP-014-CS`
* **Course:** Parallel and Distributed Computing (PADC)

---

## 📌 Assignment Overview
This repository implements all the core concurrency concepts introduced in **Chapter 2 (Thread-based Parallelism)** of the *Python Parallel Programming Cookbook*. Everything is integrated and modularized cleanly within a single execution script (`implementation.py`).

### 🧩 Implemented Concepts:
1. **Thread Definition & Identification:** Spawning threads using `threading.Thread`, inspecting thread names, active counts, and OS Process IDs (`os.getpid()`).
2. **Custom Thread Subclassing:** Creating dedicated thread classes by inheriting from `threading.Thread` and overriding the `run()` method.
3. **Locks & Reentrant Locks (`Lock` & `RLock`):** Securing critical sections and preventing race conditions during shared resource access.
4. **Semaphores (`Semaphore`):** Throttling and limiting concurrent thread execution over limited resources.
5. **Events (`Event`):** Signaling state changes and flags across separate execution threads.
6. **Conditions (`Condition`):** Implementing multi-thread notification and producer-consumer conditional waiting.
7. **Barriers (`Barrier`):** Synchronizing multiple threads at a shared checkpoint before proceeding.
8. **Thread-Safe Queues (`queue.Queue`):** Safe data exchange between producer and consumer threads.

---

## 💻 How to Run
Execute the unified implementation script via terminal:
```bash
python implementation.py
