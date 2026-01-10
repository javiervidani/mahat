# שאלה 6

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

## שאלה 6 (15 נקודות)

מפעל לייצור דגלים של מדינות שונות מעוניין במערכת ניהול מלאי ממוחשבת.

לשם כך הוגדרה המחלקה "דגל" (Flag) ולה התכונות האלה:
• שם מדינה (country) - מחרוזת (String)
• אורך (length) - מספר שלם (int)
• רוחב (width) - מספר שלם (int)

במחלקה הוגדרה פעולה בונה המקבלת ערכים לכל התכונות והפעולות get/set ו-toString.

### א. (3 נק')
הגדירו מחלקה בשם "מחסן דגלים" (Warehouse) הכוללת את התכונות האלה:
• מערך של דגלים (flags) - מערך של עצמים מסוג "דגל" (Flag) בגודל מקסימלי של 100.
• מערך של כמויות (quantities) - מערך של מספרים שלמים (int) באותו הגודל כמו מערך הדגלים, כאשר כל תא מציין את הכמות של הדגל המתאים במערך הדגלים (הדגל במקום ה-i במערך הדגלים מתאים לכמות במקום ה-i במערך הכמויות).
• מספר הדגלים הנוכחי במחסן (currentFlags) - מספר שלם (int).

כתבו פעולה בונה למחלקה המאתחלת את מערך הדגלים ומערך הכמויות בגודל 100 ואת מספר הדגלים הנוכחי ל-0.

### ב. (4 נק')
כתבו במחלקה "מחסן דגלים" פעולה המקבלת שם מדינה, אורך ורוחב של דגל ומספר דגלים ומוסיפה את הדגל למחסן. אם כבר קיים דגל זהה במחסן, הפעולה תעדכן את הכמות שלו. אם המחסן מלא, הפעולה תדפיס הודעה מתאימה.

כותרת הפעולה:
```java
public void add(String country, int length, int width, int quant)
```

### ג. (4 נק')
כתבו במחלקה "מחסן דגלים" פעולה המקבלת מספר שלם המייצג כמות מינימלית ומדפיסה את שמות הפרטים של כל הדגלים שכמותם במחסן קטנה מהכמות המינימלית.

כותרת הפעולה:
```java
public void flagsWithMinQuantity(int minQuality)
```

### ד. (4 נק')
לקראת ביקור של ראשי מדינות שונות יש להכין דגלים לקישוט העיר. כתבו במחלקה "מחסן דגלים" פעולה המקבלת רשימה של שמות מדינות (מערך של מחרוזות) ומדפיסה עבור כל מדינה ברשימה את כמות הדגלים שלה הקיימים במחסן. שימו לב שבמחסן יכולים להיות דגלים שונים של אותה המדינה!

כותרת הפעולה:
```java
public void printFlags(String[] countries)
```

## פתרון

### סעיף א (3 נקודות)

```java
public class Warehouse {
    private Flag[] flags;
    private int[] quantities;
    private int currentFlags;
    
    public Warehouse() {
        flags = new Flag[100];
        quantities = new int[100];
        currentFlags = 0;
    }
}
```

### סעיף ב (4 נקודות)

```java
// פעולת עזר במחלקה Flag
public boolean equals(Flag other) {
    return this.country.equals(other.country) &&
           this.length == other.length &&
           this.width == other.width;
}

// במחלקה Warehouse
public void add(String country, int length, int width, int quant) {
    Flag newFlag = new Flag(country, length, width);
    
    // בדיקה אם הדגל כבר קיים
    for (int i = 0; i < currentFlags; i++) {
        if (flags[i].equals(newFlag)) {
            quantities[i] += quant;
            return;
        }
    }
    
    // בדיקה אם המחסן מלא
    if (currentFlags >= 100) {
        System.out.println("Warehouse is full. Cannot add new flag.");
        return;
    }
    
    // הוספת דגל חדש
    flags[currentFlags] = newFlag;
    quantities[currentFlags] = quant;
    currentFlags++;
}
```

### סעיף ג (4 נקודות)

```java
public void flagsWithMinQuantity(int minQuantity) {
    System.out.println("Flags with quantity less than " + minQuantity + ":");
    for (int i = 0; i < currentFlags; i++) {
        if (quantities[i] < minQuantity) {
            System.out.println(flags[i].toString() + " - Quantity: " + quantities[i]);
        }
    }
}
```

### סעיף ד (4 נקודות)

```java
public void printFlags(String[] countries) {
    System.out.println("Total flag quantities per country:");
    for (String country : countries) {
        int total = 0;
        for (int i = 0; i < currentFlags; i++) {
            if (flags[i].getCountry().equals(country)) {
                total += quantities[i];
            }
        }
        System.out.println(country + ": " + total + " flag(s)");
    }
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
**ניהול מלאי של דגלים** בשלוש שכבות:
1. **Flag**: מדינה, אורך, רוחב (עצם דגל בודד)
2. **Warehouse**: מערך של דגלים שונים + כמויות לכל דגל + מס' סוגי דגלים
3. דרישות: הוספה, חיפוש כפולויות, עדכון כמויות, דיווח

### שלבי פתרון:

**סעיף א - בנאי Warehouse:**
- אתחל שני מערכים בגודל 100
- אתחל currentFlags ל-0 (עוקב)

**סעיף ב - add (הוספה/עדכון):**
1. צור עצם Flag חדש
2. עבור כל דגל קיים: בדוק אם זהה (country, length, width)
3. אם מצאת דגל זהה: עדכן כמות, חזור
4. אם לא מצאת וגם המחסן לא מלא: הוסף דגל חדש
5. אם מלא: הדפס שגיאה

**סעיף ג - flagsWithMinQuantity (דיווח על מעט):**
1. לולאה על כל דגל קיים
2. בדוק אם כמותו < minQuantity
3. אם כן: הדפס את שם המדינה ופרטי דגל

**סעיף ד - printFlags (סכום לפי מדינה):**
1. עבור כל מדינה ברשימה שהתקבלה:
   - צבור סכום כמויות של כל דגלים עם מדינה זו
   - הדפס

### דגשים חשובים:
- **equals() צריך 3 בדיקות**: country, length, width (כל זה צריך להיות זהה)
- **בדיקת דגל קיים מתבצעת לפני בדיקת מקום בחסן**
- **currentFlags משמש כעוקב** - הוא גם אינדקס ליום קלט וגם מס' דגלים
- **printFlags עובדת עם מדינות שמופיעות בפרמטר**, לא כל המדינות במחסן

### תנאי קצה:
- מחסן ריק (currentFlags = 0)
- מחסן מלא (currentFlags = 100)
- דגל קיים: עדכן כמות (לא הוסף)
- מדינה שלא במחסן: צפה כמות = 0

### טעויות נפוצות:
1. **equals() לא נכון** - צריך להשוות שלוש תכונות, לא אחת
2. **הוספת דגל קיים שוב** - צריך לעדכן קיים, לא להוסיף חדש
3. **לא בדיקת מקום בחסן** לפני הוספה
4. **פרינט בplaintText** - צריך ל-toString() או פרטים מסודרים
5. **flagsWithMinQuantity** - דפיסה של דגלים שמספרם **קטן** מ-min, לא **גדול**

### דוגמה עבודה:
```java
Warehouse w = new Warehouse();
w.add("Israel", 100, 50, 5);      // הוסף דגל חדש
w.add("Israel", 100, 50, 3);      // עדכן כמות ל-8
w.flagsWithMinQuantity(10);        // דפיס Israel (8 < 10)
String[] countries = {"Israel", "USA"};
w.printFlags(countries);           // Israel: 8, USA: 0
```

### סיבוכיות:
- **add**: O(n) - בדיקה בכל דגלים
- **flagsWithMinQuantity**: O(n) - סריקת כל דגלים
- **printFlags**: O(m × n) - m מדינות, n דגלים בחסן

### סיכום:
התרגיל בודק:
- ניהול **מערכים מקבילים** (flags ו-quantities)
- השוואה **כוללת** (equals עם 3 תנאים)
- **שימוש בעוקב** (currentFlags)
- **עדכון כמויות** ללא כפילות

**סעיף ב - add(country, length, width, quant):**
```java
public void add(String country, int length, int width, int quant) {
    Flag newFlag = new Flag(country, length, width);
    
    // בדוק אם קיים
    for (int i = 0; i < currentFlags; i++) {
        if (flags[i].equals(newFlag)) {
            quantities[i] += quant;  // עדכן כמות
            return;
        }
    }
    
    // בדוק אם מלא
    if (currentFlags >= 100) {
        System.out.println("Warehouse is full");
        return;
    }
    
    // הוסף חדש
    flags[currentFlags] = newFlag;
    quantities[currentFlags] = quant;
    currentFlags++;
}
```

**סעיף ג - flagsWithMinQuantity(minQuantity):**
```java
public void flagsWithMinQuantity(int minQuantity) {
    for (int i = 0; i < currentFlags; i++) {
        if (quantities[i] < minQuantity) {
            System.out.println(flags[i] + ", quantity: " + quantities[i]);
        }
    }
}
```

**סעיף ד - printFlags(countries):**
```java
public void printFlags(String[] countries) {
    for (String country : countries) {
        int total = 0;
        for (int i = 0; i < currentFlags; i++) {
            if (flags[i].getCountry().equals(country))
                total += quantities[i];
        }
        System.out.println(country + ": " + total);
    }
}
```

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מחסן ריק (currentFlags = 0)
- מחסן מלא (currentFlags = 100)
- דגל כפול (אותו שם+אורך+רוחב)
- מדינה שלא קיימת ב-printFlags

✅ **טעויות נפוצות:**
1. **שכחה לקרוא equals()** לבדיקת דגל זהה (לא ==!)
   - צריך להשוות country + length + width
2. **עדכון כמות בדגל קיים בלי return** → יוסיף דגל כפול!
3. **לא בדוק אם מחסן מלא** לפני הוספה
4. **printFlags צריך סכימה** של כל דגלים עם אותה מדינה
5. **בדיקת equals()** צריכה גם אורך + רוחב!

✅ **דוגמאות בדיקה:**
```
addFlag("USA", 100, 50, 10)     // הוסף דגל אמריקאי
addFlag("USA", 100, 50, 5)      // עדכן כמות → 15
addFlag("France", 100, 50, 20)  // דגל שונה
flagsWithMinQuantity(8)          // ידפיס France (20 < סף)
printFlags({"USA", "France"})    // USA: 15, France: 20
```

---