import hashlib
import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(page_title="مولد مفاتيح التفعيل", page_icon="🔑", layout="centered")

# النص السري الخاص بك (يجب أن يطابق الكود الموجود في تطبيق الـ React Native مستقبلاً)
SECRET_SALT = "ONSPACE_SECURE_KEY_2026"


def generate_license_key(device_id: str) -> str:
    clean_id = device_id.strip().upper()
    raw_str = f"{clean_id}-{SECRET_SALT}"
    hash_obj = hashlib.sha256(raw_str.encode()).hexdigest().upper()
    return f"{hash_obj[:4]}-{hash_obj[4:8]}-{hash_obj[8:12]}-{hash_obj[12:16]}"


# واجهة المستخدم
st.title("🔑 لوحة توليد مفاتيح التفعيل")
st.write("أدخل رمز الجهاز (Device ID) الخاص بالعميل لتوليد مفتاح التفعيل:")

device_id_input = st.text_input("رمز الجهاز (Device ID):", placeholder="مثال: A1B2-C3D4-E5F6")

if st.button("توليد مفتاح التفعيل", type="primary"):
    if device_id_input:
        license_key = generate_license_key(device_id_input)
        st.success("تم توليد المفتاح بنجاح!")
        st.code(license_key, language="text")
    else:
        st.warning("يرجى إدخال رمز الجهاز أولاً.")