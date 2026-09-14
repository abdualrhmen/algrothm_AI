# ========================================================
# مقرر: ذكاء اصطناعي (عملي)
# التكليف الأول: بنية البيانات Stack و Queue والتحقق قبل الحذف
# إعداد الطالب: عبدالرحمن علي احمد فرحان
# ========================================================

# 1. بنية المكدس (Stack)
print("--- تجربة بنية المكدس (Stack) ---")
myStack = [1, 21, 32, 45]
print("المكدس الأولي:", myStack)

def pop_from_stack(stack):
    if len(stack) == 0:
        print("تحذير: المكدس فارغ! لا يمكن تنفيذ عملية الحذف (Stack Underflow).")
        return None
    else:
        item = stack.pop()
        print(f"تم حذف العنصر: {item} من قمة المكدس.")
        return item

while len(myStack) > 0:
    pop_from_stack(myStack)

print("\nمحاولة الحذف من مكدس فارغ:")
pop_from_stack(myStack)

# 2. بنية الطابور (Queue)
print("\n" + "="*50)
print("--- تجربة بنية الطابور (Queue) ---")
myQueue = [1, 21, 32, 45]
print("الطابور الأولي:", myQueue)

def dequeue(queue):
    if len(queue) == 0:
        print("تحذير: الطابور فارغ! لا يمكن تنفيذ عملية الحذف (Queue Underflow).")
        return None
    else:
        item = queue.pop(0)
        print(f"تم حذف العنصر: {item} من مقدمة الطابور.")
        return item

while len(myQueue) > 0:
    dequeue(myQueue)

print("\nمحاولة الحذف من طابور فارغ:")
dequeue(myQueue)