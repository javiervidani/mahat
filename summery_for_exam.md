# יסודות Java למבחן מה״ט – תקציר ממוקד

> חוברת סיכום ממוקדת למבחן מה״ט באלגוריתמיקה ו‑Java

## תוכן העניינים
- 1. מבנה תוכנית Java
- 2. משתנים וסוגי נתונים
- 3. תנאים (if/else)
- 4. לולאות (for/while)
- 5. מערכים חד־ממדיים
- 6. מחרוזות (String)
- 7. פונקציות (פעולות)
- 8. מערך דו־ממדי (מטריצה)
- 9. רקורסיה – עקרונות
- נספח א׳ – פונקציות שימושיות למבחן
- טיפי זהב למבחן מה״ט

---

## 1. מבנה תוכנית Java
```java
public class Main {
    public static void main(String[] args) {
        // קוד
    }
}
```
- כל תוכנית רצה מתוך `main`
- כל קוד חייב להיות בתוך מחלקה

---

## 2. משתנים וסוגי נתונים
- `int` – מספרים שלמים
- `double` – מספרים עשרוניים
- `char` – תו יחיד
- `boolean` – true / false
- `String` – מחרוזת

```java
int x = 5;
double y = 2.5;
char c = 'a';
boolean ok = true;
String s = "hello";
```

---

## 3. תנאים (if / else)
```java
if (x > 0) {
    System.out.println("חיובי");
} else {
    System.out.println("שלילי");
}
```

טיפים למבחן:
- תמיד סוגר סוגריים
- השוואה: `==` ולא `=`

---

## 4. לולאות

### for
```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

### while
```java
int i = 0;
while (i < 10) {
    i++;
}
```

---

## 5. מערכים חד־ממדיים
```java
int[] arr = {1,2,3,4};
```

גישה:
```java
arr[i]
arr.length
```

סריקה:
```java
for (int i = 0; i < arr.length; i++) {
    // arr[i]
}
```

---

## 6. מחרוזות (String)

```java
String s = "Ab3d";
int len = s.length();
char ch = s.charAt(i);
```

בדיקות נפוצות:
```java
ch >= 'a' && ch <= 'z'
ch >= 'A' && ch <= 'Z'
ch >= '0' && ch <= '9'
```

---

## 7. פונקציות (פעולות)

מבנה:
```java
public static int func(int x) {
    return x + 1;
}
```

קריאה:
```java
int y = func(5);
```

---

## 8. מערך דו־ממדי (מטריצה)

```java
int[][] mat = {
    {1,2,3},
    {4,5,6}
};
```

סריקה:
```java
for (int i = 0; i < mat.length; i++) {
    for (int j = 0; j < mat[i].length; j++) {
        mat[i][j];
    }
}
```

---

## 9. רקורסיה – עקרונות
- תנאי עצירה
- קריאה לעצמה

```java
public static int fact(int n) {
    if (n == 0) return 1;
    return n * fact(n-1);
}
```

---

# נספח א׳ – פונקציות שימושיות למבחן

## מספר מקסימלי במערך
```java
public static int max(int[] arr) {
    int max = arr[0];
    for (int i = 1; i < arr.length; i++)
        if (arr[i] > max) max = arr[i];
    return max;
}
```

---

## בדיקת פלינדרום
```java
public static boolean isPalindrome(String s) {
    int i = 0, j = s.length()-1;
    while (i < j) {
        if (s.charAt(i) != s.charAt(j)) return false;
        i++; j--;
    }
    return true;
}
```

---

## ספירת ספרות במחרוזת
```java
public static int countDigits(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        char ch = s.charAt(i);
        if (ch >= '0' && ch <= '9') count++;
    }
    return count;
}
```

---

## ספירת אותיות a-z במחרוזת (תדירויות)
```java
public static int[] countLettersAZ(String s) {
    int[] freq = new int[26];
    for (int i = 0; i < s.length(); i++) {
        char ch = Character.toLowerCase(s.charAt(i));
        if (ch >= 'a' && ch <= 'z') {
            freq[ch - 'a']++;
        }
    }
    return freq;
}
```

דוגמה שימוש:
```java
int[] f = countLettersAZ("Hello Java");
// f[0] מכיל את מספר הפעמים של 'a', f[1] עבור 'b', ...
```

---

## בדיקת מערך ממוין
```java
public static boolean isSorted(int[] arr) {
    for (int i = 0; i < arr.length-1; i++)
        if (arr[i] > arr[i+1]) return false;
    return true;
}
```

---

## בדיקת מספר ראשוני
```java
public static boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i*i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
```

---

## נקודת איזון במערך (Balance Index)

**נוסח טיפוסי:**
נתון מערך מספרים. נקודת איזון היא אינדקס שבו מכפלת האיברים משמאל שווה למכפלת האיברים מימין.

```java
public static int balanceIndex(int[] arr) {
    for (int k = 0; k < arr.length; k++) {
        int left = 1, right = 1;

        for (int i = 0; i < k; i++)
            left *= arr[i];

        for (int i = k + 1; i < arr.length; i++)
            right *= arr[i];

        if (left == right)
            return k;
    }
    return -1;
}
```

🔑 הערה למבחן: מדובר **בכפל**, לא סכום.

---

## הצפנת מחרוזת – "סטופיד"

שלבים:

1. הסרת רווחים
2. החלפת זוגות תווים סמוכים
3. היפוך המחרוזת

```java
public static String stupidEncrypt(String s) {
    String noSpaces = "";
    for (int i = 0; i < s.length(); i++)
        if (s.charAt(i) != ' ')
            noSpaces += s.charAt(i);

    String swapped = "";
    for (int i = 0; i < noSpaces.length() - 1; i += 2)
        swapped = noSpaces.charAt(i + 1) + "" + noSpaces.charAt(i) + swapped;

    if (noSpaces.length() % 2 == 1)
        swapped = noSpaces.charAt(noSpaces.length() - 1) + swapped;

    return swapped;
}
```

---

## Word Search – חיפוש מילה במטריצה

```java
public static boolean wordSearch(char[][] mat, String word) {
    for (int i = 0; i < mat.length; i++)
        for (int j = 0; j < mat[i].length; j++)
            if (check(mat, word, i, j))
                return true;
    return false;
}
```

*(הפעולה check בודקת 4 כיוונים: ימין, שמאל, מעלה, מטה)*

---

## מספרים ראשוניים – זוגות לפי גולדבך

```java
public static int countPrimePairs(int num) {
    int count = 0;
    for (int i = 2; i <= num / 2; i++)
        if (isPrime(i) && isPrime(num - i))
            count++;
    return count;
}
```

---

## רקורסיה – ספרה מקסימלית במספר

```java
public static int maxDigit(int n) {
    if (n < 10) return n;
    int d = n % 10;
    int max = maxDigit(n / 10);
    return d > max ? d : max;
}
```

---

## רקורסיה – ספירת ספרות

```java
public static int countDigits(int n) {
    if (n < 10) return 1;
    return 1 + countDigits(n / 10);
}
```

---

## עבודה עם מערך אובייקטים (OOP)

```java
public static void printAboveAvg(Employee[] arr) {
    double sum = 0;
    int count = 0;

    for (Employee e : arr)
        if (e.isEngineer()) {
            sum += e.getSalary();
            count++;
        }

    double avg = sum / count;

    for (Employee e : arr)
        if (e.isWorker() && e.getSalary() > avg)
            System.out.println(e.getId());
}
```

---

## מיומנות חובה: ניתוח פעולה (What עושה?)

בדיקה:

* מה מאותחל לפני הלולאה
* מה משתנה בכל איטרציה
* מה מוחזר בסוף

🔴 אין לכתוב קוד – רק להסביר.

---

## טיפי בונוס למבחן ⭐

* אל תדלג על תנאי קצה
* העדף קוד ברור על קצר
* רקורסיה = תנאי עצירה ראשון
* במטריצה: תמיד mat.length ו־mat[i].length

---

## החלפת שני איברים במערך (Swap)

נפוץ במיונים, What, Secret.

```java
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
```

---

## 2️⃣ היפוך מערך / היפוך מחרוזת

```java
for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
```

---

## 3️⃣ ספירה עם תנאי (Counter Pattern)

```java
int count = 0;
for (int i = 0; i < arr.length; i++) {
    if (condition)
        count++;
}
```

---

## 4️⃣ חיפוש אינדקס ראשון שעומד בתנאי

```java
for (int i = 0; i < arr.length; i++) {
    if (condition)
        return i;
}
return -1;
```

---

## 5️⃣ סינון / העתקת מערך

```java
int[] b = new int[arr.length];
int k = 0;

for (int i = 0; i < arr.length; i++) {
    if (condition)
        b[k++] = arr[i];
}
```

---

## מעבר נכון על String

```java
for (int i = 0; i < s.length(); i++) {
    char ch = s.charAt(i);
}
```

❌ לא `s[i]`
❌ לא `length(s)`

---

## בנאי בסיסי (Constructor)

```java
public class Account {
    private int id;
    private String password;

    public Account(int id, String password) {
        this.id = id;
        this.password = password;
    }
}
```

---

## Getter / Setter בסיסיים

```java
public int getId() {
    return id;
}

public void setPassword(String p) {
    password = p;
}
```

---

## foreach על מערך אובייקטים

```java
for (Employee e : arr) {
    System.out.println(e.getId());
}
```

---

## הדפסה נכונה

```java
System.out.println(result);
```

---

## 🧠 כלל זהב למבחן

> אם זיהית בשאלה תבנית שמופיעה במסמך הזה – אתה בדרך לפתרון הנכון.

---

### סטטוס מוכנות

✔ מערכים
✔ מחרוזות
✔ לולאות
✔ תנאים
✔ OOP בסיסי
✔ רקורסיה (מעקב והבנה)

אם הכל כאן ברור – אתה מוכן למבחן מה"ט Java.


---


## טיפי זהב למבחן מה״ט ⭐
- תמיד בדוק `length` ולא מספר קבוע
- לא לשכוח `return`
- לא לערבב בין אינדקס לערך
- ברקורסיה – קודם תנאי עצירה
- בשאלה "מה הפעולה עושה" – חפש תבנית

---
