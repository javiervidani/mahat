# שאלה 9

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 9 (15 נקודות)

החברה "סע לך" מוכרת כרטיסי טיסה ליעדים שונים ברחבי העולם.

לצורך אחסון נתוני כרטיסים שנמכרו הוגדרה מחלקה בשם Destination ולה 3 תכונות:
• שם היעד – name – מסוג מחרוזת String.
• מחיר כרטיס – price – מסוג מספר ממשי double.
• מספר כרטיסים שנמכרו – num – מסוג מספר שלם int.

לפניכם מחלקה TestDestination המשתמשת במחלקה Destination:

```java
public class TestDestination {
    public static double total(Destination d) {
        return d.getPrice() * d.getNum();
    }
    
    public static void main(String[] args) {
        Destination d1 = new Destination("Paris");
        d1.setName("London");
        d1.setNum(200);
        d1.setPrice(300.0);
        System.out.println(total(d1));
        
        d1.setNum(50);
        Destination d2 = new Destination(d1.getName(), 100.0, d1.getNum());
        System.out.println(total(d2));
    }
}
```

### א. (4 נק')
כתבו במחלקה Destination כותרות של כל הפעולות הנדרשות לביצוע הפעולה הראשית main.

### ב. (3 נק')
עקבו אחרי הביצוע של הפעולה הראשית main ורשמו מה יהיה הפלט.

### ג. (4 נק')
כתבו במחלקה TestDestination פעולה המקבלת מערך יעדים dest (מערך של עצמים מסוג Destination) ומחזירה שם יעד שמספר הכרטיסים שנמכרו עבורו הוא הנמוך ביותר.

כותרת הפעולה:
```java
public static String getNotPopular(Destination[] dest)
```

### ד. (4 נק')
כתבו במחלקה TestDestination פעולה המקבלת מערך יעדים dest (מערך של עצמים מסוג Destination) ומחיר maxPrice. הפעולה תחזיר מערך של שמות היעדים אשר מחיר כרטיס הטיסה אליהם הינו נמוך מ-maxPrice, אם אין אף יעד כזה, הפעולה תחזיר מערך בגודל 0.

כותרת הפעולה:
```java
public static String[] cheapDests(Destination[] dest, double maxPrice)
```

## פתרון

*הפתרון לשאלה זו לא נסרק במלואו בקובץ הפתרונות*

### סעיף ב (3 נקודות) - פלט התוכנית:

```
60000.0
5000.0
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מחלקת Destination מייצגת יעד טיסה עם שם, מחיר כרטיס, ומספר כרטיסים שנמכרו.  
צריך לכתוב כותרות, לעקוב אחרי ביצוע, ולכתוב מתודות לחיפוש.

### אלגוריתם:

**סעיף א - כותרות נדרשות:**

מתוך main רואים:
1. `new Destination("Paris")` → **Constructor עם שם בלבד**
2. `d1.setName("London")` → **Setter לשם**
3. `d1.setNum(200)` → **Setter למספר כרטיסים**
4. `d1.setPrice(300.0)` → **Setter למחיר**
5. `d1.getName()` → **Getter לשם**
6. `d1.getNum()` → **Getter למספר כרטיסים**
7. `d1.getPrice()` → **Getter למחיר**
8. `new Destination(name, price, num)` → **Constructor עם 3 פרמטרים**

```java
public Destination(String name)
public Destination(String name, double price, int num)
public String getName()
public void setName(String name)
public double getPrice()
public void setPrice(double price)
public int getNum()
public void setNum(int num)
```

**סעיף ב - מעקב אחרי main:**

```java
Destination d1 = new Destination("Paris");
d1.setName("London");     // name="London"
d1.setNum(200);           // num=200
d1.setPrice(300.0);       // price=300.0
System.out.println(total(d1));  // 300.0 * 200 = 60000.0

d1.setNum(50);            // num=50 (עדכון!)
Destination d2 = new Destination(d1.getName(), 100.0, d1.getNum());
// d2: name="London", price=100.0, num=50
System.out.println(total(d2));  // 100.0 * 50 = 5000.0
```

**פלט:**
```
60000.0
5000.0
```

**סעיף ג - getNotPopular:**

מטרה: מצא את שם היעד עם **הכי פחות** כרטיסים שנמכרו.

```java
public static String getNotPopular(Destination[] dest) {
    int minIndex = 0;  // הנחה: היעד הראשון הוא המינימום
    
    for (int i = 1; i < dest.length; i++) {
        if (dest[i].getNum() < dest[minIndex].getNum()) {
            minIndex = i;  // מצאנו יעד עם פחות מכירות
        }
    }
    
    return dest[minIndex].getName();
}
```

**דוגמה:**
- `dest = [{"Paris", 300, 200}, {"London", 100, 50}, {"NYC", 500, 150}]`
- מינימום: "London" עם 50 כרטיסים

**סעיף ד - cheapDests:**

מטרה: החזר מערך שמות של יעדים שמחירם **נמוך מ-maxPrice**.

```java
public static String[] cheapDests(Destination[] dest, double maxPrice) {
    // שלב 1: ספור כמה יעדים זולים יש
    int count = 0;
    for (int i = 0; i < dest.length; i++) {
        if (dest[i].getPrice() < maxPrice) {
            count++;
        }
    }
    
    // שלב 2: אם אין - החזר מערך ריק
    if (count == 0)
        return new String[0];
    
    // שלב 3: צור מערך בגודל מדויק והעתק שמות
    String[] result = new String[count];
    int index = 0;
    for (int i = 0; i < dest.length; i++) {
        if (dest[i].getPrice() < maxPrice) {
            result[index++] = dest[i].getName();
        }
    }
    
    return result;
}
```

**דוגמה:**
- `dest = [{"Paris", 300}, {"London", 100}, {"NYC", 500}, {"Rome", 80}]`
- `maxPrice = 200`
- תוצאה: `{"London", "Rome"}` (מחירים 100 ו-80)

### 🎯 מה להקפיד:

✅ **תנאי קצה בסעיף ג:**
- מערך ריק: נניח שלא יקרה (או נבדוק arr.length)
- כל היעדים עם אותו מספר כרטיסים: יחזיר את הראשון
- מערך עם יעד אחד: יחזיר אותו

✅ **תנאי קצה בסעיף ד:**
- אין יעדים זולים: **חובה** להחזיר `new String[0]` לא `null` ⚠️
- כל היעדים זולים: כל השמות יוחזרו
- maxPrice=0: אף יעד לא יעבור (מחירים חיוביים)

✅ **טעויות נפוצות:**
- **בסעיף ב**: שכחה לעקוב אחרי `d1.setNum(50)` לפני יצירת d2
- **בסעיף ג**: 
  - אתחול minIndex לא נכון (מ-1 במקום 0)
  - שימוש ב-`>` במקום `<` (מחפש מקסימום במקום מינימום)
  - החזרת האינדקס במקום השם
- **בסעיף ד**:
  - החזרת null במקום מערך ריק
  - שכחת ספירה ראשונית → יצירת מערך גדול מדי עם nullים
  - שימוש ב-`<=` במקום `<` ("נמוך מ-" לא "עד")
  - אי-אתחול index=0 לפני מילוי המערך

✅ **דוגמאות בדיקה:**
- **total**: `dest("Paris", 50.0, 10)` → 500.0
- **getNotPopular**: `[{100 sold}, {50 sold}, {200 sold}]` → יעד עם 50
- **cheapDests**: maxPrice=100 עם [{50},{150},{80}] → [{50},{80}]

---