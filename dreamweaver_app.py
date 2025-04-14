import streamlit as st
import random
from datetime import datetime

# הגדרות ראשוניות של הדף
st.set_page_config(page_title="DreamWeaver - אפליקציית חלומות", page_icon="🌙", layout="wide")

# --- כותרת ראשית ---
st.title("DreamWeaver 🌙")
st.markdown("**חולמים אחרת. חיים אחרת.**")
st.divider()

# --- שאלות למשתמש לפני השינה ---
st.header("🛌 שאלון לפני שינה")

col1, col2 = st.columns(2)

with col1:
    mood = st.selectbox("איך הרגשת היום?", ["שמח 😊", "עצבני 😠", "עייף 🤪", "נרגש 🤩", "רגיל 😐"])
    energy = st.radio("מה רמת האנרגיה שלך?", ["נמוכה", "בינונית", "גבוהה"])
    dream_type = st.radio("מה סוג החלום שאתה מחפש?", ["מרגיע", "מעורר השראה", "הרפתקני", "רומנטי", "מפתיע"])     
    focus = st.text_input("על מה היית רוצה שהמוח יתמקד במהלך השינה?")

with col2:
    sleep_time = st.slider("מתי אתה מתכוון להירדם? (שעה)", 0, 23, 23)
    music = st.checkbox("🎵 תרצה מוזיקה מרגיעה ברקע?")
    breathing = st.checkbox("🧘 תרגול נשימות לפני השינה?")
    together = st.checkbox("🫡 חולמים ביחד עם מישהו?")

# --- פונקציית יצירת תסריט חלום ---
def generate_dream_script():
    base = f"אתה מוצא את עצמך ב{random.choice(['יער קסום', 'חוף שקט', 'עיר צבעונית', 'טירה ישנה', 'עולם מרחף'])}, בזמן שהשמש {random.choice(['שוקעת לאיטה', 'זורחת בין ההרים', 'נעלמת בין העננים'])}."
    emotion = f" אתה מרגיש {mood.replace(' �', '').lower()}, עם אנרגיה {energy} ובלבך רצון ל{dream_type}."
    focus_line = f" אתה חושב על {focus if focus else 'מה שבא'} ומאפשר לתת-מודע להנחות אותך."
    together_line = " לידך נמצא אדם קרוב שגם הוא חולם איתך... 💕" if together else ""
    music_line = " מוזיקה שקטה ברקע עוטפת אותך בתחושת שלווה... 🎶" if music else ""
    return base + emotion + focus_line + together_line + music_line

# --- תוצאה ---
st.divider()
st.header(":sparkles: החלום שלך מוכן!")

if st.button("צור לי חלום מותאם!"):
    script = generate_dream_script()
    st.success("החלום הותאם עבורך בהצלחה!")
    st.markdown(f"#### תסריט החלום שלך:")
    st.markdown(f"""
    > {script}
    """)
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", caption="חלום בהתהוות...", use_column_width=True)

    if breathing:
        st.markdown("""
        ### 🧘 תרגול נשימות
        קח נשימה עמוקה... החזק... ושחרר לאט.
        חזור על הפעולה 5 פעמים.
        """)

# --- מדריך שימוש ---
st.divider()
with st.expander("🔧 מדריך שימוש באפליקציה"):
    st.markdown("""
    1. ענה על כל השאלות בכנות ובשלווה.
    2. לחץ על כפתור יצירת החלום.
    3. קרא את התסריט והיכנס לאווירה.
    4. אם בחרת, שים מוזיקה והתחל תרגול נשימות.
    5. עצום עיניים... ושיהיה לילה חלומי 🌚
    """)

# --- תיאור תחתון ---
st.divider()
st.caption("פותח באהבה על ידי DreamWeaver Team ❤️")
st.caption(f"גרסה 1.0 | {datetime.now().strftime('%Y-%m-%d')}")
