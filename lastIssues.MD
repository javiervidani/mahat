## דוגמאות קוד — הסברים קצרים

להלן הקבצים וקטעי הקוד מסודרים: לכל קטע יש כותרת קצרה, שורה אחת של הסבר, בלוק קוד עם fence ו'---' כמפריד בין דוגמאות.

---

### 1) מיון בבחירה (Selection Sort)
אלגוריתם מיון בבחירה עובר על המערך ומאתר בכל איטרציה את האיבר הקטן ביותר מהחלק הלא-ממויין, ומחליף אותו עם האיבר הראשון הלא-ממויין. כך בכל סיבוב המינימום "עולה" למקומו הנכון. מתאים למערכים קטנים, לא יעיל למערכים גדולים.
```java
public static void selectionSort(int[] arr) {
    // לולאה ראשית — עוברת על כל איבר פרט לאחרון
    for (int i = 0; i < arr.length - 1; i++) {
        int minIndex = i; // מניח שהאיבר הנוכחי הוא המינימום
        // לולאה פנימית — מחפשת את המינימום בחלק הלא-ממויין
        for (int j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) // אם נמצא איבר קטן יותר — מעדכן את המינימום
                minIndex = j;
        }
        // מחליף בין האיבר הנוכחי למינימום שמצאנו
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}
```

---

### 2) בדיקת מרחק 3 (hasDistanceThree)
הפונקציה בודקת האם קיימים שני איברים שווים במערך שמרחקם זה מזה בדיוק 3 אינדקסים. שימושי למציאת דפוסים או קשרים בין איברים במערך.
```java
public static boolean hasDistanceThree(int[] arr) {
    // לולאה ראשית — עוברת על כל איבר
    for (int i = 0; i < arr.length; i++) {
        // לולאה פנימית — משווה לכל איבר אחר אחרי i
        for (int j = i + 1; j < arr.length; j++) {
            if (arr[i] == arr[j] && j - i == 3) // בודק אם הערכים שווים והמרחק בדיוק 3
                return true; // מצאנו זוג מתאים
        }
    }
    return false; // אם לא נמצא — מחזיר false
}
```

---

### 3) סכום ספרות זוגיות/אי-זוגיות
הקוד מפריד את סכום הספרות הזוגיות והאי-זוגיות במספר נתון. עובר על כל ספרה, בודק אם היא זוגית או אי-זוגית ומוסיף לסכום המתאים. שימושי לניתוח מספרים או אימותים.
```java
int num = 4267; // המספר לבדיקה
int sumEven = 0; // סכום ספרות זוגיות
int sumOdd = 0; // סכום ספרות אי-זוגיות

while (num > 0) {
    int digit = num % 10; // מוציא ספרה אחרונה

    if (digit % 2 == 0)
        sumEven += digit; // אם זוגית — מוסיף לסכום הזוגי
    else
        sumOdd += digit; // אם אי-זוגית — מוסיף לסכום האי-זוגי

    num /= 10; // מסיר את הספרה האחרונה
}
// דוגמה: עבור 4267 — ספרות: 7,6,2,4
// סכום זוגיות: 6+2+4=12
// סכום אי-זוגיות: 7
```

---

### 4) הדפסת ספרות (Print Digits)
הקוד מדפיס את כל הספרות של מספר מהספרה האחרונה לראשונה, באמצעות חלוקה חוזרת ב-10. מתאים להצגת ספרות בנפרד או לניתוח מספרים.
```java
int num = 4267; // המספר לבדיקה

while (num > 0) {
    int digit = num % 10; // מוציא ספרה אחרונה
    System.out.println(digit); // מדפיס את הספרה
    num = num / 10; // מסיר את הספרה האחרונה
}
```

---

### 5) מיון ונפרוד מספרים זוגיים/אי-זוגיים
הפונקציה מפצלת את המערך למערכי משנה של זוגיים ואי-זוגיים, ממיינת כל קבוצה בנפרד, ולבסוף מאחדת אותן למערך אחד. מדגים עקרון של עיבוד קבוצות שונות בנפרד.
```java
public static int[] sortEvenOdd(int[] arr) {
    int[] even = new int[arr.length]; // מערך לאיברים זוגיים
    int[] odd = new int[arr.length]; // מערך לאיברים אי-זוגיים
    int e = 0, o = 0; // מונים לאינדקסים
    // מפריד איברים לפי זוגיות
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0)
            even[e++] = arr[i]; // מוסיף למערך הזוגי
        else
            odd[o++] = arr[i]; // מוסיף למערך האי-זוגי
    }
    // ממיין את המערך הזוגי
    for (int i = 0; i < e - 1; i++)
        for (int j = 0; j < e - 1 - i; j++)
            if (even[j] > even[j + 1]) {
                int t = even[j]; // שומר את הערך הזוגי
                even[j] = even[j + 1]; // מחליף
                even[j + 1] = t; // מחליף
            }
    // ממיין את המערך האי-זוגי
    for (int i = 0; i < o - 1; i++)
        for (int j = 0; j < o - 1 - i; j++)
            if (odd[j] > odd[j + 1]) {
                int t = odd[j]; // שומר את הערך האי-זוגי
                odd[j] = odd[j + 1]; // מחליף
                odd[j + 1] = t; // מחליף
            }
    // מאחד את המערכים לתוצאה
    int[] result = new int[arr.length];
    int k = 0;
    for (int i = 0; i < o; i++)
        result[k++] = odd[i]; // מוסיף את האי-זוגיים
    for (int i = 0; i < e; i++)
        result[k++] = even[i]; // מוסיף את הזוגיים
    return result;
}
```

---

### 6) פיצול מערך לשניים (דוגמה תבנית)
תבנית לפיצול מערך לשני חלקים לפי תנאי כלשהו. מדגים כיצד לאסוף איברים לשני מערכים שונים בהתאם לתנאי.
```java
// Dividing an array into two
int a = 0, b = 0;
for (int i = 0; i < arr.length; i++) {
    if (condition)
        arrA[a++] = arr[i];
    else
        arrB[b++] = arr[i];
}
```

---

### 7) השוואת שני מערכים (תבנית)
תבנית להשוואת ערכים בין שני מערכים. בודק האם כל איבר במערך הראשון קטן או שווה לאיבר המקביל במערך השני. שימושי לבדיקות סדר או השוואות.
```java
// Comparing two arrays
for (int i = 0; i < arrA.length; i++) {
    if (arrA[i] <= arrB[i]) return false;
}
return true;
```

---

### 8) בדיקת סדר בערכים זוגיים
הקוד בודק האם הערכים הזוגיים במערך מסודרים בסדר עולה. עובר על כל איבר זוגי ומשווה אותו לקודמו. מתאים לבדיקות סדר חלקיות.
```java
// Based on even values
int prev = -1;
for (int i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
        if (prev != -1 && arr[i] < prev) return false;
        prev = arr[i];
    }
}
return true;
```

---

### 9) בדיקת סדר באינדקסים זוגיים
הקוד בודק האם הערכים באינדקסים זוגיים (0,2,4,...) מסודרים בסדר עולה. עובר על כל אינדקס זוגי ומשווה אותו לקודמו.
```java
// Based on even indices
for (int i = 2; i < arr.length; i += 2) {
    if (arr[i] < arr[i - 2]) return false;
}
return true;
```

---

### 10) תבנית לבדיקה אחידה
תבנית לולאה לבדיקת תנאי זהה לכל איבר במערך. מדגים כיצד לבדוק אחידות או עמידה בתנאי מסוים לכל איבר.
```java
// Template for checking uniformity
for (int i = 1; i < arr.length; i++) {
    if (!sameCondition) return false;
}
return true;
```

---

### 11) תבנית לספירה לפי תנאי
תבנית לספירה של כמה איברים במערך מקיימים תנאי מסוים. שימושי לסטטיסטיקות או ניתוח נתונים.
```java
// Template for counting elements matching a condition
int count = 0;
for (int i = 0; i < arr.length; i++) {
    if (condition) {
        count++;
    }
}
return count;
```

---

### 12) דוגמת קונסטרקטור מיוחד
דוגמה לקונסטרקטור שמאתחל שדות ברירת מחדל לאובייקט. מדגים כיצד להגדיר ערכים ראשוניים לאובייקט חדש.
```java
// Special constructor example
public StorageBox(double cost) {
    this.cost = cost;
    this.color = "white";
    this.hasCover = false;
    this.length = rand;
    this.width = rand;
    this.height = rand;
}
```

---

### 13) מבנה כיתה סטנדרטי
תבנית לכיתה עם שדות, קונסטרקטור וגטרים/סטטרים. מדגים מבנה בסיסי של מחלקה ב-Java, כולל שדות פרטיים ומתודות גישה.
```java
// Standard class example
class StorageBox {
    private String color;
    private int length, width, height;
    private double cost;
    private boolean hasCover;

    public StorageBox(...) {
        // Assignments
    }

    // Getters and setters
}
```

---

### 14) יצירת מספר אקראי בטווח
הקוד מייצר מספר אקראי בטווח בין X ל-Y כולל. שימושי למשחקים, סימולציות או בדיקות.
```java
// Random number generation example
int num = X + (int)(Math.random() * (Y - X + 1));
```

---

### 15) סכום ספרות של מספר
הקוד מחשב את סכום כל הספרות במספר נתון. עובר על כל ספרה ומוסיף לסכום הכללי. מתאים לניתוח מספרים.
```java
// Sum of digits example
int temp = num;
int sumDigits = 0;

while (temp > 0) {
    sumDigits += temp % 10;
    temp /= 10;
}
```

---

### 16) דוגמת תלמידים — הדפסת מעל הממוצע
דוגמה מלאה: מחלקת `Student` ופונקציה שמדפיסה את ה-IDs של תלמידים עם ציון מעל הממוצע. מדגים עבודה עם מחלקות, חישוב ממוצע, וסינון איברים לפי תנאי.
```java
public class Student {
    int id;
    int grade;

    public Student(int id, int grade) {
        this.id = id;
        this.grade = grade;
    }
}

public class Test {

    public static void printAboveAverage(Student[] arr) {
        if (arr == null || arr.length == 0) {
            System.out.println("No students in the array.");
            return;
        }

        // 1. Compute average grade
        int sum = 0;
        for (Student s : arr) {
            sum += s.grade;
        }
        double average = sum / (double) arr.length;

        // 2. Print IDs of students with grades above average
        for (Student s : arr) {
            if (s.grade > average) {
                System.out.println(s.id);
            }
        }
    }

    public static void main(String[] args) {
        Student[] students = new Student[]{
            new Student(1, 80),
            new Student(2, 70),
            new Student(3, 90)
        };

        printAboveAverage(students); // Outputs 1 and 3
    }
}
```
