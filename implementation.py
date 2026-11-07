"""
PADC Assignment - Chapter 2: Comprehensive Python Multithreading Cookbook
Student Name: Muhammad Tayyab
Student ID: 24SP-014-CS

Description:
This single script implements all core Chapter 2 concepts from the Python
Parallel Programming Cookbook:
1. Thread Definition, Naming, and Process ID Identification
2. Custom Thread Class Subclassing
3. Mutual Exclusion (Lock & RLock)
4. Semaphores for resource throttling
5. Events for thread signaling
6. Conditions for multi-thread coordination
7. Barriers for synchronization checkpoints
8. Thread-safe Queues for producer-consumer communication
"""

import threading
import time
import random
import queue
import os

# -------------------------------------------------------------
# 1. Thread Definition, Naming, and Process ID Demonstration
# -------------------------------------------------------------
def basic_worker():
    t_name = threading.current_thread().name
    t_id = threading.get_ident()
    pid = os.getpid()
    print(f"[Concept 1] Running thread '{t_name}' (ID: {t_id}) in Process ID: {pid}")
    time.sleep(0.1)

def demo_thread_definition():
    print("\n--- 1. Thread Definition & Identification Demo ---")
    t = threading.Thread(target=basic_worker, name="CustomNamedWorker")
    t.start()
    t.join()
    print(f"Active threads count: threading.active_count() = {threading.active_count()}")


# -------------------------------------------------------------
# 2. Custom Thread Class Subclassing
# -------------------------------------------------------------
class MyCustomThread(threading.Thread):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        print(f"[Concept 2] Custom Thread subclass started with message: '{self.message}'")
        time.sleep(0.1)
        print(f"[Concept 2] Custom Thread subclass finished execution.")

def demo_custom_thread():
    print("\n--- 2. Custom Thread Class Subclassing Demo ---")
    custom_t = MyCustomThread("Hello from Subclassed Thread!")
    custom_t.start()
    custom_t.join()


# -------------------------------------------------------------
# 3. Lock & RLock Demonstration
# -------------------------------------------------------------
shared_counter = 0
counter_lock = threading.Lock()
reentrant_lock = threading.RLock()

def recursive_increment(val):
    with reentrant_lock:
        if val > 0:
            global shared_counter
            shared_counter += 1
            recursive_increment(val - 1)

def demo_locks():
    print("\n--- 3. Lock & RLock Demonstration ---")
    global shared_counter
    shared_counter = 0
    
    def increment_with_lock():
        global counter_lock, shared_counter
        with counter_lock:
            temp = shared_counter
            time.sleep(0.01)
            shared_counter = temp + 1

    threads = [threading.Thread(target=increment_with_lock) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"[Concept 3] Final counter with Lock: {shared_counter}")

    recursive_increment(3)
    print(f"[Concept 3] Counter after RLock recursive increments: {shared_counter}")


# -------------------------------------------------------------
# 4. Semaphore Demonstration
# -------------------------------------------------------------
semaphore = threading.Semaphore(2)

def limited_resource_access(thread_id):
    print(f"[Concept 4] Thread-{thread_id} trying to acquire semaphore...")
    with semaphore:
        print(f"[Concept 4] Thread-{thread_id} ACQUIRED semaphore. Processing...")
        time.sleep(0.2)
        print(f"[Concept 4] Thread-{thread_id} releasing semaphore.")

def demo_semaphore():
    print("\n--- 4. Semaphore Demonstration (Max 2 concurrent) ---")
    threads = [threading.Thread(target=limited_resource_access, args=(i,)) for i in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()


# -------------------------------------------------------------
# 5. Event Demonstration
# -------------------------------------------------------------
event = threading.Event()

def waiter_thread():
    print("[Concept 5] Waiter thread waiting for the event signal...")
    event.wait()
    print("[Concept 5] Waiter thread received the event signal! Resuming work.")

def setter_thread():
    print("[Concept 5] Setter thread preparing setup...")
    time.sleep(0.2)
    print("[Concept 5] Setter thread is SETTING the event now!")
    event.set()

def demo_event():
    print("\n--- 5. Event Signaling Demonstration ---")
    event.clear()
    t1 = threading.Thread(target=waiter_thread)
    t2 = threading.Thread(target=setter_thread)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# -------------------------------------------------------------
# 6. Condition Demonstration
# -------------------------------------------------------------
condition = threading.Condition()
condition_data_ready = False

def consumer(name):
    global condition_data_ready
    with condition:
        print(f"[Concept 6] {name} waiting for data condition...")
        while not condition_data_ready:
            condition.wait()
        print(f"[Concept 6] {name} consumed the data condition!")

def producer():
    global condition_data_ready
    time.sleep(0.2)
    with condition:
        print("[Concept 6] Producer generating data and notifying...")
        condition_data_ready = True
        condition.notify_all()

def demo_condition():
    print("\n--- 6. Condition Demonstration ---")
    global condition_data_ready
    condition_data_ready = False
    c1 = threading.Thread(target=consumer, args=("Consumer-1",))
    c2 = threading.Thread(target=consumer, args=("Consumer-2",))
    p = threading.Thread(target=producer)
    c1.start()
    c2.start()
    p.start()
    c1.join()
    c2.join()
    p.join()


# -------------------------------------------------------------
# 7. Barrier Demonstration
# -------------------------------------------------------------
barrier = threading.Barrier(3)

def runner_at_barrier(id):
    print(f"[Concept 7] Runner {id} running towards the barrier...")
    time.sleep(random.uniform(0.1, 0.3))
    print(f"[Concept 7] Runner {id} reached the barrier, waiting for others.")
    barrier.wait()
    print(f"[Concept 7] Runner {id} crossed the barrier and sprinted to the finish!")

def demo_barrier():
    print("\n--- 7. Barrier Synchronization Demonstration ---")
    threads = [threading.Thread(target=runner_at_barrier, args=(i,)) for i in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()


# -------------------------------------------------------------
# 8. Threading with Queue Demonstration
# -------------------------------------------------------------
def producer_task(q):
    for item in range(3):
        q.put(item)
        print(f"[Concept 8] Queue Producer put item {item}")
        time.sleep(0.1)
    q.put(None)

def consumer_task(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"[Concept 8] Queue Consumer processed item {item}")
        q.task_done()

def demo_queue():
    print("\n--- 8. Thread-Safe Queue Demonstration ---")
    q = queue.Queue()
    p = threading.Thread(target=producer_task, args=(q,))
    c = threading.Thread(target=consumer_task, args=(q,))
    p.start()
    c.start()
    p.join()
    c.join()


# -------------------------------------------------------------
# Main Execution Runner
# -------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 65)
    print(" PADC Assignment: Chapter 2 Cookbook Comprehensive Implementation")
    print(f" Student Name: Muhammad Tayyab | Student ID: 24SP-014-CS")
    print("=" * 65)

    demo_thread_definition()
    demo_custom_thread()
    demo_locks()
    demo_semaphore()
    demo_event()
    demo_condition()
    demo_barrier()
    demo_queue()

    print("\n" + "=" * 65)
    print(" All Chapter 2 Cookbook concepts successfully demonstrated!")
    print("=" * 65)



