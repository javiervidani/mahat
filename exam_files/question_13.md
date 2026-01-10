# שאלה 13

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 13 (11 נקודות)

ברשת מכללות "דרך למקצוע" קיימות 80 מכללות. ברשת הוחלט לבנות מאגר מידע כדי לעזור לרוצים ללמוד מחשב לבחור את המכללה המתאימה ביותר לצרכים שלהם.

לכל מכללה שמורים הפרטים הבאים:
• שם מכללה.
• יישוב שבו נמצא קמפוס לימודי של המכללה.
• מערך המגמות שנלמדות במכללה. בכל מכללה יש לכל היותר עשר מגמות שונות.

כל מגמה מזוהה ע"י מספר המקצוע (code) ושם מגמה (majName).

### א. (3 נק')
כתבו את כותרת המחלקה ואת התכונות עבור כל אחת מהמחלקות:
• מגמה - Major
• מכללה - College
• רשת מכללות - Network

### ב. (4 נק')
כתבו פעולה פנימית במחלקה Network המקבלת שם יישוב ומדפיסה את שמותיהן של כל המכללות אשר נמצאות ביישוב זה. אם אין אף מכללה של הרשת ביישוב, יש להדפיס הודעה מתאימה.

### ג. (4 נק')
הנהלת הרשת בודקת אפשרות לפתוח מגמה חדשה. כתבו פעולה פנימית במחלקה Network המקבלת קוד של המגמה ומחזירה מערך שמות של המכללות שבהן אפשר לפתוח את המגמה.

אם אין אף מכללה שבה אפשר לפתוח את המגמה יש להחזיר ערך null.

**שימו לב:** אי אפשר לפתוח מגמה אם היא כבר קיימת במכללה או שבמכללה יש כבר 10 מגמות שונות.

**הערה:** אם כתבתם פעולות עזר – עליכם לציין באיזו מחלקה הן נמצאות וגם להגדיר את טענות הכניסה והיציאה לכל פעולה (הפרמטרים של הפעולה והמטרה שלה).

## פתרון

### סעיף א (3 נקודות)

```java
public class Major {
    private String majName;
    private int code;
}

public class College {
    private String name;
    private String city;
    private Major[] majorArr;
}

public class Network {
    private College[] colleges;
}
```

### סעיף ב (4 נקודות)

```java
public void printCities(String city) {
    int cnt = 0;
    for (int i = 0; i < this.colleges.length; i++)
        if (this.colleges[i].getCity().equals(city)) {
            cnt++;
            System.out.println(colleges[i].getName());
        }
        
    if (cnt == 0)
        System.out.println("No colleges!!");
}
```

### סעיף ג (4 נקודות)

```java
public String[] canOpenNewMajor(int code) {
    int cnt = 0;
    String res = "";
    boolean found;
    
    for (int i = 0; i < this.colleges.length; i++) {
        found = false;
        if (this.colleges[i].getMajorArr().length < 10) {
            for (int j = 0; j < this.colleges[i].getMajorArr().length; j++)
                if (this.colleges[i].getMajorArr()[j].getCode() == code)
                    found = true;
                    
            if (!found)
                res = res + " " + this.colleges[i].getName();
        }
    }
    
    if (res.equals(""))
        return null;
        
    return res.split("\\s+");
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מערכת ניהול רשת מכללות (80 מכללות) עם מגמות לימוד. צריך:  
1. להגדיר 3 מחלקות: Major, College, Network  
2. לחפש מכללות ביישוב מסוים  
3. למצוא מכללות שיכולות לפתוח מגמה חדשה

### אלגוריתם:

**סעיף א - הגדרת המחלקות:**

```java
public class Major {
    private String majName;  // שם המגמה
    private int code;        // קוד המקצוע
}

public class College {
    private String name;         // שם המכללה
    private String city;         // יישוב
    private Major[] majorArr;    // מערך מגמות (עד 10)
}

public class Network {
    private College[] colleges;  // מערך 80 מכללות
}
```

**עקרונות תכנון:**
- Major: מגמה בודדת (שם + קוד)
- College: מכללה מכילה **מערך של מגמות** (composition)
- Network: רשת מכילה **מערך של מכללות** (composition)

**סעיף ב - printCities:**

מטרה: הדפס שמות כל המכללות ב**יישוב נתון**.

```java
public void printCities(String city) {
    int cnt = 0;  // מונה מכללות שנמצאו
    
    for (int i = 0; i < this.colleges.length; i++) {
        if (this.colleges[i].getCity().equals(city)) {
            cnt++;
            System.out.println(colleges[i].getName());
        }
    }
    
    if (cnt == 0)
        System.out.println("No colleges!!");
}
```

**לוגיקה:**
1. עבור על כל המכללות
2. השווה יישוב עם city (שימוש ב-equals לא ==)
3. אם תואם - הדפס שם + ספור
4. אם לא נמצאה אף מכללה - הדפס הודעה

**דוגמה:**
```
colleges = [{"TAU", "Tel Aviv"}, {"BGU", "Beer Sheva"}, {"Afeka", "Tel Aviv"}]
printCities("Tel Aviv") → הדפס: TAU, Afeka
printCities("Haifa") → הדפס: "No colleges!!"
```

**סעיף ג - canOpenNewMajor:**

מטרה: מצא מכללות ש**יכולות** לפתוח מגמה עם קוד code.

תנאים לפתיחה:
1. המגמה עם code **לא קיימת** כבר במכללה
2. במכללה **פחות מ-10 מגמות** (יש מקום)

```java
public String[] canOpenNewMajor(int code) {
    int cnt = 0;
    String res = "";  // נצבור שמות
    boolean found;
    
    // שלב 1: עבור על כל המכללות
    for (int i = 0; i < this.colleges.length; i++) {
        found = false;
        
        // בדוק אם יש מקום (פחות מ-10 מגמות)
        if (this.colleges[i].getMajorArr().length < 10) {
            
            // בדוק אם המגמה כבר קיימת
            for (int j = 0; j < this.colleges[i].getMajorArr().length; j++) {
                if (this.colleges[i].getMajorArr()[j].getCode() == code) {
                    found = true;  // המגמה כבר קיימת!
                    break;
                }
            }
            
            // אם לא קיימת - הוסף למחרוזת התוצאה
            if (!found)
                res = res + " " + this.colleges[i].getName();
        }
    }
    
    // אם לא נמצאו מכללות מתאימות
    if (res.equals(""))
        return null;
    
    // המר מחרוזת למערך (פיצול לפי רווחים)
    return res.split("\\s+");
}
```

**לוגיקה מפורטת:**
```
לכל מכללה:
    אם יש מקום (<10 מגמות):
        חפש את code במערך המגמות
        אם לא נמצא:
            הוסף שם המכללה לתוצאה
            
אם התוצאה ריקה:
    החזר null
אחרת:
    פצל מחרוזת למערך והחזר
```

**דוגמה:**
```
מכללה A: 5 מגמות, אין code=101 → ✅ יכולה לפתוח
מכללה B: 10 מגמות → ❌ אין מקום
מכללה C: 7 מגמות, יש code=101 → ❌ כבר קיימת
מכללה D: 8 מגמות, אין code=101 → ✅ יכולה לפתוח

תוצאה: {"A", "D"}
```

### 🎯 מה להקפיד:

✅ **טעויות נפוצות בהגדרת מחלקות:**
- שכחת private למשתנים
- Major[] במקום Major בתוך College
- College[] במקום College בתוך Network
- אי-הגדרת getter/setter נדרשים

✅ **טעויות נפוצות ב-printCities:**
- שימוש ב-`==` במקום `equals` להשוואת מחרוזות ❌
- אי-הדפסת הודעה כש-cnt==0
- הדפסת cnt במקום שם המכללה
- שכחת אתחול cnt

✅ **טעויות נפוצות ב-canOpenNewMajor:**
- **החזרת מערך ריק במקום null**: השאלה מבקשת **null** במפורש!
- לולאה פנימית שלא נעצרת אחרי מציאת code (ללא break)
- בדיקת `== 10` במקום `< 10` (10 בדיוק זה מלא!)
- בדיקת `>= 10` תעבוד אבל `< 10` יותר ברור
- שכחת split - החזרת מחרוזת במקום מערך
- שימוש ב-`split(" ")` במקום `split("\\s+")` - לא יטפל במספר רווחים

✅ **טריק split:**
```java
"A B C".split(" ")   → {"A", "B", "C"} ✅
"A  B   C".split(" ") → {"A", "", "B", "", "", "C"} ❌ (רווחים כפולים)
"A  B   C".split("\\s+") → {"A", "B", "C"} ✅ (מטפל בכל רווח)
```

✅ **גישה חלופית ב-canOpenNewMajor (יעילה יותר):**
במקום מחרוזת, ספור תחילה כמה מכללות מתאימות, צור מערך בגודל מדויק:
```java
// ספירה ראשונה
int count = 0;
for (...) if (canOpen) count++;

if (count == 0) return null;

// יצירת מערך בגודל מדויק
String[] result = new String[count];
int index = 0;
for (...) if (canOpen) result[index++] = name;

return result;
```

✅ **תנאי קצה:**
- אין מכללות ביישוב: הדפס "No colleges!!"
- אין מכללות שיכולות לפתוח: החזר `null`
- כל המכללות מלאות (10 מגמות): החזר `null`
- המגמה קיימת בכל המכללות: החזר `null`
- מכללה ללא מגמות (length=0): יכולה לפתוח ✅

✅ **דוגמאות בדיקה:**
```java
// דוגמה למבנה נתונים
Major m1 = new Major("CS", 101);
Major m2 = new Major("Math", 102);
Major[] majors1 = {m1, m2};  // 2 מגמות

College c1 = new College("TAU", "Tel Aviv", majors1);

printCities("Tel Aviv")  → "TAU"
canOpenNewMajor(103)     → {"TAU"} (יש מקום, אין 103)
canOpenNewMajor(101)     → null או מערך ללא TAU (101 כבר קיים)
```

---