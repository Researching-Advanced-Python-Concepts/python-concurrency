# threads can also suffer race condition due to a bug with timing

# while using threading.Condition we must acquire the condition
# b4 we can call wait or notify
