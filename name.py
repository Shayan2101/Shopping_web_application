import re  


def validate_persian_name(name):  
    # الگوی regex برای بررسی نام فارسی  
    pattern = r'^[ آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیئ\s]+$'  
    
    # بررسی تطابق با الگو  
    if re.match(pattern, name):  
        return True  
    else:  
        return False  
# تست نام‌ها  
test_names = ['سلام', 'مرحبا', 'سلام123', 'سلام!']
for name in test_names:  
    if validate_persian_name(name):  
        print(f"{name} - معتبر")  
    else:  
        print(f"{name} - نامعتبر")