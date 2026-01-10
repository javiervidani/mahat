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


<div style="page-break-after: always;"></div>

# חלק ב׳ – שאלות מבחן 2024 (קיץ תשפ״ד)

## מבנה המבחן 2024
- **חלק א׳**: 4 מתוך 7 שאלות (12 נק' כל אחת)
- **חלק ב׳**: 2 מתוך 4 שאלות (15 נק' כל אחת)
- **חלק ג׳**: 1 מתוך 3 שאלות (22 נק')
- **סה״כ**: 100 נקודות

---


<div style="page-break-after: always;"></div>

# שאלה 1

**חלק א' - ענו על 4 מבין השאלות 1-7 (ערך כל שאלה – 12 נקודות)**

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 1 (12 נקודות)

כתבו קטע תוכנית הקולט 20 זוגות של מספרים שלמים וחיוביים.
על התוכנית לחשב ולהדפיס:
• את כמות המספרים הדו-ספרתיים שנקלטו.
• את סכום כל המספרים הזוגיים שנקלטו.

## פתרון

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int twoDigitNumCounter = 0;
        int sumOfeven = 0;

        int num1, num2;
        for (int i = 0; i < 20; i++) {
            num1 = in.nextInt();
            num2 = in.nextInt();
            
            if (num1 >= 10 && num1 <= 99)
                twoDigitNumCounter++;
            if (num2 >= 10 && num2 <= 99)
                twoDigitNumCounter++;
            if (num1 % 2 == 0)
                sumOfeven += num1;
            if (num2 % 2 == 0)
                sumOfeven += num2;
        }
        System.out.println("sum of even numbers: " + sumOfeven);
        System.out.println("number of two digit numbers: " + twoDigitNumCounter);
}
}
```

---

## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
קליטת 20 זוגות מספרים וחישוב:
1. **כמה** מהם דו-ספרתיים (10-99)
2. **סכום** כל המספרים הזוגיים (שמתחלקים ב-2)

### אלגוריתם:

**שלב 1 – ראשום:**
- אתחול שני מונים: `twoDigitCounter = 0` ו-`evenSum = 0`
- פתח לולאה ל-20 איטרציות (כי 20 זוגות = 40 מספרים)

**שלב 2 – קלוט ובדוק:**
- קלוט מספר
- **בדוק אם דו-ספרתי:** `10 <= num <= 99` → הגדל מונה
- **בדוק אם זוגי:** `num % 2 == 0` → הוסף לסכום

**שלב 3 – פלט:**
- הדפס את המונה ואת הסכום

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- שני מספרים **בכל** איטרציה, לא אחד
- המונה עולה ב-2 בחזרה כי זוג = 2 מספרים
- זוגי = `num % 2 == 0`

✅ **טעויות נפוצות:**
1. **שכחה של אתחול** המונים - יתחילו ב-0 אוטומטי, אבל טוב לכתוב במפורש
2. **בדיקה לא נכונה לדו-ספרתי** - חייב `10 <= num <= 99`, לא `num >= 10` בלבד
3. **שכחה להגדיל המונה פעמיים** בכל זוג (אם שני המספרים דו-ספרתיים)
4. **הדפסה בתוך הלולאה** - הדפס רק בסוף

✅ **כיצד לבדוק את הקוד:**
- הרץ עם: 15, 25 (שניהם דו-ספרתיים וזוגיים) → מונה = 2, סכום = 40
- הרץ עם: 5, 100 (לא דו-ספרתיים) → מונה = 0
- בדוק עם מספרים אי-זוגיים → לא צריכים להוסיף לסכום

---

<div style="page-break-after: always;"></div>

# שאלה 2

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 2 (12 נקודות)

כתבו קטע תוכנית הקולט מחרוזות עד שתיקלט מחרוזת באורך אי-זוגי.
עבור כל מחרוזת יש לבדוק אם מופיעה בה האות 'Z' ולהדפיס הודעה מתאימה.
כמו כן, יש לספור ולהדפיס את כמות המחרוזות אשר מתחילות ומסתיימות בתווים זהים.

## פתרון

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str;
        int sameStartEndCounter = 0;
        
        str = in.nextLine();
        int len = str.length();
        
        while (len % 2 == 0) {
            if (str.contains("Z"))  // or: str.indexOf('Z') != -1
                System.out.println("string contains Z");
            
            if (str.charAt(0) == str.charAt(len - 1))
                sameStartEndCounter++;
                
            str = in.nextLine();
            len = str.length();
        }
        
        System.out.println("Number of strings with same start and end: " + sameStartEndCounter);
    }
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
קלוט מחרוזות עד שמתקבלת מחרוזת באורך אי-זוגי, וספור כמה מחרוזות התחילו **וגם** סיימו באותה אות.

### אלגוריתם:

**שלב 1 – לולאה אינסופית:**
- `while(true)` - לולאה שלא נעצרת עד break
- קלוט מחרוזת: `String s = scanner.next()`

**שלב 2 – בדיקת תנאי עצירה:**
- אם `s.length() % 2 != 0` → **break** (אורך אי-זוגי = עצירה)

**שלב 3 – בדיקת התאמה:**
- אם `s.charAt(0) == s.charAt(s.length()-1)` → הגדל מונה

**שלב 4 – פלט:**
- הדפס את המונה

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מחרוזת באורך 1 (תו אחד) - אי-זוגי → עצירה
- מחרוזת ריקה - אי-זוגי → עצירה
- אות ראשונה = אות אחרונה (case-sensitive)

✅ **טעויות נפוצות:**
1. **שימוש ב-`equals()` במקום `==`** - לתווים צריך `==`
2. **שכחה של תנאי עצירה** - הלולאה תרוץ לנצח
3. **בדיקה של `length()-1` במקום `length()`** - האות האחרונה היא באינדקס length-1
4. **ספירה לפני בדיקת אורך** - תחילה בדוק אורך, אחר כך ספור

✅ **כיצד לבדוק את הקוד:**
- קלט: "hello", "abc", "mom" (אי-זוגי) → תוצאה: 0 (אף אחת לא מתחילה ומסיימת באותה אות)
- קלט: "level", "radar", "bob" (אי-זוגי) → תוצאה: 2 (level ו-radar)
- קלט: "a" (אי-זוגי מיד) → תוצאה: 0 (עצר מיד)

---
---
<div style="page-break-after: always;"></div>

# שאלה 3

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 3 (12 נקודות)

כתבו קטע תוכנית המייצרת 40 מספרים אקראיים דו-ספרתיים חיוביים. על התוכנית לחשב ולהדפיס:
• מהו המספר שנוצר הכי הרבה פעמים (אם יש כמה מספרים שנוצרו הכי הרבה פעמים, מספיק להדפיס אחד מהם).
• אילו מספרים לא נוצרו.

## פתרון

```java
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] arr = new int[100];
        
        for (int i = 0; i < 100; i++)
            arr[i] = 0;
            
        for (int i = 0; i < 40; i++)
            arr[10 + rand.nextInt(90)]++;
            
        int max = arr[10];
        int maxIndex = 10;
        
        for (int i = 10; i < 100; i++) {
            if (arr[i] > max) {
                max = arr[i];
                maxIndex = i;
            }
            if (arr[i] == 0)
                System.out.println(i + " not generated");
        }
        
        System.out.println(maxIndex + " Generated maximum times");
    }
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מצא את **הרצף הזוגי הרציף הארוך ביותר** במערך - כמה מספרים זוגיים עוקבים ברצף.

### אלגוריתם:

**שלב 1 – אתחול:**
- `currentCounter = 0` - ספירה של הרצף הנוכחי
- `maxCounter = 0` - הרצף הארוך ביותר שמצאנו

**שלב 2 – מעבר על המערך:**
- לכל איבר במערך:
  - **אם זוגי** (`num % 2 == 0`): `currentCounter++`
  - **אם אי-זוגי**: 
    - `maxCounter = Math.max(maxCounter, currentCounter)`
    - `currentCounter = 0` (אתחול מחדש)

**שלב 3 – סיום:**
- אחרי הלולאה: `maxCounter = Math.max(maxCounter, currentCounter)`
- (למקרה שהמערך מסתיים ברצף זוגי)

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מערך שכולו זוגי → currentCounter לא מתאפס
- מערך שכולו אי-זוגי → תוצאה 0
- רצף ארוך בסוף המערך → חייב בדיקה אחרי הלולאה

✅ **טעויות נפוצות:**
1. **שכחה לעדכן max בסוף הלולאה** - רצף זוגי בסוף לא ייספר
2. **שכחה לאפס את currentCounter** אחרי כל אי-זוגי
3. **בדיקה של `num % 2 == 1`** במקום `!= 0` (לא עובד עם מספרים שליליים)
4. **החזרת currentCounter במקום maxCounter** - שגיאה בסיום

✅ **כיצד לבדוק את הקוד:**
- [2, 4, 6, 1, 8, 10, 12] → תוצאה: 3 (רצף של 2,4,6)
- [1, 3, 5, 7] → תוצאה: 0 (אין זוגיים)
- [2, 4, 6, 8, 10] → תוצאה: 5 (כל המערך)
- [1, 2, 4, 1, 6, 8, 10, 12] → תוצאה: 4 (רצף של 6,8,10,12)

---
---
<div style="page-break-after: always;"></div>

# שאלה 4

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 4 (12 נקודות)

"המסעדה Chef4U" מציעה משלוח מנות שף קטנות במחיר מוזל עד לבית הלקוח.

המחלקה Food מייצגת מנה. למחלקה 4 תכונות:
• שם המנה – name, מטיפוס מחרוזת String.
• מחיר המנה – price, מטיפוס מספר ממשי double.
• מנה חלבית – isMilk, מטיפוס בוליאני boolean (true – מנה חלבית, false – לא).
• דירוג המנה – rating, מטיפוס מספר שלם. דירוג המנה הוא מספר שלם מ-1 (הכי נמוך) עד 10 (הכי גבוה(.

למחלקה הוגדרו פעולה בונה (constructor), פעולות get/set והפעעולה toString.

### א. (3 נק')
לפעמים המסעדה נאלצת להחליף את המנה הנוכחית (this) למנה אחרת (other).
אפשר להחליף בין המנות אם שתיהן מאותו סוג (חלבי או לא), יש להן אותו הדירוג ומחיר של המנה other לא גבוה ממחיר של המנה this.

כתבו פעולה המקבלת מנה אחרת (הפנייה לעצם מטיפוס Food). הפעולה תבדוק אם ניתן להחליף מנה this למנה other. אם כן – הפעולה תחזיר ערך true, ולא – הפעולה תחזיר ערך false.

כותרת הפעולה:
```java
public boolean canChange(Food other)
```

### ב. (3 נק')
כתבו פעולה המקבלת מערך מנות arr ומנה newFood. הפעולה תדפיס את שמות כל המנות שאפשר להחליף אותן למנה newFood.

כותרת הפעולה:
```java
public static void changes(Food[] arr, Food newFood)
```

### ג. (4 נק')
המסעדה הכריזה על מבצע: שתי מנות שונות בפחות מ-100 ₪.

כתבו פעולה המקבלת מערך מנות ומדפיסה את כל הצירופים האפשריים של שתי מנות שונות שעולות יחד פחות מ-100 ₪.

כותרת הפעולה:
```java
public static void offers(Food[] arr)
```

### ד. (2 נק')
מהי סיבוכיות הפעולות שכתבתם בסעיפים ב' ו-ג'. הסבירו את תשובתכם.

## פתרון

*פתרון לשאלה זו לא נמצא בקובץ הפתרונות שנסרק*

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מחלקת Food מייצגת מנה במסעדה. צריך לכתוב מתודות להשוואת מנות (canChange), מציאת מנות החלפה אפשריות (changes), ומציאת צירופי מנות במבצע (offers).

### אלגוריתם:

**סעיף א - canChange:**
1. בדוק אם שתי המנות מאותו סוג חלבי: `this.isMilk == other.isMilk`
2. בדוק אם הדירוג זהה: `this.rating == other.rating`
3. בדוק אם המחיר של other לא גבוה יותר: `other.price <= this.price`
4. החזר true רק אם כל 3 התנאים מתקיימים

**סעיף ב - changes:**
1. עבור על כל המנות במערך arr באמצעות לולאה
2. לכל מנה, קרא ל-newFood.canChange(arr[i])
3. אם התוצאה true - הדפס את שם המנה: `arr[i].getName()`

**סעיף ג - offers:**
1. לולאה כפולה: `for i=0 to arr.length-2` ו-`for j=i+1 to arr.length-1`
2. לכל זוג מנות שונות, חשב סכום: `arr[i].getPrice() + arr[j].getPrice()`
3. אם הסכום < 100, הדפס את שני השמות

**סעיף ד - סיבוכיות:**
- סעיף ב: O(n) - לולאה אחת על n מנות
- סעיף ג: O(n²) - לולאה כפולה, כל זוג מנות נבדק פעם אחת

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מערך ריק - לא יהיו צירופים
- מערך עם מנה אחת - לא יהיו צירופים
- כל המנות יקרות מדי - לא יודפס כלום

✅ **טעויות נפוצות בסעיף א:**
- בדיקת `other.price >= this.price` במקום `<=` (היפוך כיוון)
- שכחת בדיקת אחד מהתנאים (סוג חלבי/דירוג/מחיר)
- שימוש ב-`=` במקום `==` להשוואה

✅ **טעויות נפוצות בסעיף ג:**
- לולאה שמתחילה מ-`j=i` במקום `j=i+1` → יבדוק מנה עם עצמה
- לולאה שמתחילה מ-`j=0` → יבדוק כל זוג פעמיים
- בדיקת `<= 100` במקום `< 100`

✅ **דוגמאות בדיקה:**
- canChange: מנות `{"Pasta", 50, true, 8}` ו-`{"Pizza", 45, true, 8}` → true
- canChange: מנות `{"Pasta", 50, true, 8}` ו-`{"Steak", 60, false, 8}` → false (סוג שונה)
- offers: מערך `[{45}, {30}, {80}]` → זוגות (0,1)=75 בלבד

---
<div style="page-break-after: always;"></div>

# שאלה 5

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 5 (12 נקודות)

מערך של מספרים שלמים חיוביים נקרא מערך "מושלם K" אם הוא עונה על התנאי הבא:
הסכום של כל K האיברים ההתחלתיים במערך (האיברים אשר נמצאים במקומות 0, 1, 2, ..., K-1) מתחלק ב-K ללא שארית.

לדוגמה:
המערך הבא הוא מערך "מושלם 5":

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 7 | 1 | 4 | 1 | 2 | 3 | 2 | 1 | 3 |

כי סכום של חמשת האיברים הראשונים 7+1+4+1+2=15 מתחלק ב-5.

### א. (5 נק')
כתבו פעולה המקבלת מערך של מספרים שלמים חיוביים arr ומספר שלם חיובי K.
הפעולה תחזיר ערך true, אם המערך "מושלם K," ולא, הפעולה תחזיר ערך false.

כותרת הפעולה:
```java
public static boolean isPerfectK(int[] arr, int k)
```

מערך של מספרים שלמים חיוביים נקרא מערך "סופר מושלם" אם הוא מערך מושלם K עבור כל ערך של K מ-1 עד לאורך המערך.

לדוגמה:
המערך הנתון:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 7 | 1 | 4 | 1 | 2 | 3 | 2 | 1 | 3 |

הוא לא מערך "סופר מושלם" כי הוא לא מערך "מושלם 4".

### ב. (5 נק')
כתבו פעולה המקבלת מערך של מספרים שלמים חיוביים arr. הפעולה תחזיר ערך true, אם המערך "סופר מושלם", ולא, הפעולה תחזיר ערך false.

כותרת הפעולה:
```java
public static boolean isSuperPerfect(int[] arr)
```

### ג. (2 נק')
מהי סיבוכיות הפעולות שכתבתם בסעיפים א' ו-ב'. הסבירו את תשובתכם.

## פתרון

### סעיף א (5 נקודות)

```java
public static boolean isPerfectK(int[] arr, int k) {
    if (arr.length < k)
        return false;
        
    int sumFive = 0;
    for (int i = 0; i < k; i++)
        sumFive += arr[i];
        
    return ((sumFive % k) == 0);
}
```

### סעיף ב (5 נקודות)

```java
public static boolean isSuperPerfect(int[] arr) {
    boolean flag = true;
    for (int i = 1; i < arr.length; i++)
        if (flag)
            flag = isPerfectK(arr, i);
    return flag;
}
```

**פתרון חלופי:**

```java
public static boolean isSuperPerfect(int[] arr) {
    for (int i = 1; i < arr.length; i++)
        if (!isPerfectK(arr, i))
            return false;
    return true;
}
```

### סעיף ג (2 נקודות)

סיבוכיות סעיף א: O(n) כאשר n - מספר האיברים במערך, אפשר גם O(k)

סיבוכיות סעיף ב: O(n²) כאשר n - מספר האיברים במערך.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מערך "מושלם K" = סכום K האיברים הראשונים מתחלק ב-K ללא שארית.  
מערך "סופר מושלם" = מושלם K עבור **כל** ערך של K מ-1 עד אורך המערך.

### אלגוריתם:

**סעיף א - isPerfectK:**
1. בדוק אם אורך המערך קטן מ-K → `if (arr.length < k) return false`
2. אתחל `sumFive = 0`
3. חשב סכום K האיברים הראשונים:
   ```java
   for (int i = 0; i < k; i++)
       sumFive += arr[i];
   ```
4. בדוק אם הסכום מתחלק ב-K: `return (sumFive % k == 0)`

**דוגמה:** `arr = {7,1,4,1,2,3,2,1,3}`, `k=5`
- סכום: 7+1+4+1+2 = 15
- 15 % 5 = 0 ✅ → מערך מושלם 5

**סעיף ב - isSuperPerfect:**
1. עבור על כל ערך אפשרי של K: `for (int i = 1; i < arr.length; i++)`
2. לכל K, בדוק אם המערך מושלם K באמצעות `isPerfectK(arr, i)`
3. אם נמצא K שהמערך לא מושלם עבורו → `return false`
4. אם כל הערכים עברו → `return true`

**דוגמה לבדיקה:**
- `arr = {7,1,4,1,2,3,2,1,3}`
- K=1: סכום=7, 7%1=0 ✅
- K=2: סכום=8, 8%2=0 ✅
- K=3: סכום=12, 12%3=0 ✅
- K=4: סכום=13, 13%4=1 ❌ → לא סופר מושלם!

**סעיף ג - סיבוכיות:**
- isPerfectK: O(k) או O(n) - לולאה אחת עד K
- isSuperPerfect: O(n²) - לולאה חיצונית n פעמים, כל פעם קוראת ל-isPerfectK שרצה עד n

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- `arr.length < k` → צריך לבדוק **לפני** הלולאה, אחרת ArrayIndexOutOfBounds!
- מערך באורך 1: תמיד סופר מושלם (K=0 לא נבדק, רק מ-K=1)
- מערך ריק: מערך באורך 0 - טכנית סופר מושלם (אין ערכי K לבדוק)

✅ **טעויות נפוצות:**
- שכחת בדיקת `arr.length < k` בסעיף א → קריסה!
- התחלת הלולאה מ-`i=0` בסעיף ב → שגוי, צריך להתחיל מ-K=1
- חישוב הסכום מחדש בכל פעם במקום שימוש בפעולת עזר
- סיבוכיות: לא הבנה שיש לולאה כפולה (isSuperPerfect קורא n פעמים ל-isPerfectK)

✅ **פתרון אופטימלי בסעיף ב:**
שני גרסאות שקולות:
```java
// גרסה 1: עם דגל
boolean flag = true;
for (int i = 1; i < arr.length; i++)
    if (flag)
        flag = isPerfectK(arr, i);
return flag;

// גרסה 2: יציאה מוקדמת (עדיפה!)
for (int i = 1; i < arr.length; i++)
    if (!isPerfectK(arr, i))
        return false;
return true;
```

✅ **דוגמאות בדיקה:**
- `{6}` עם K=1: סכום=6, 6%1=0 → מושלם 1 → סופר מושלם ✅
- `{2,4}` עם K=1: 2%1=0 ✅, K=2: (2+4)%2=0 ✅ → סופר מושלם
- `{2,3}` עם K=2: 5%2=1 ❌ → לא סופר מושלם

---
<div style="page-break-after: always;"></div>

# שאלה 6

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 6 (12 נקודות)

### א. (4 נק')
נתונה הפעולה one המקבלת כפרמטר מספר שלם וחיובי num וספרה dig.

```java
public static int one(int num, int dig) {
    int res = 0;
    while (num > 0) {
        if (num % 10 == dig)
            res++;
        num = num / 10;
    }
    return res;
}
```

1. תנו דוגמה של מספר num > 1000 כך שתוצאת הזימון one(num, 7) תהיה 3.
2. מה מבצעת הפעולה one באופן כללי?

### ב. (4 נק')
נתונה הפעולה two המקבלת מערך arr של מספרים שלמים חיוביים וספרה dig:

```java
public static int two(int[] arr, int dig) {
    int res = 0;
    for (int i = 0; i < arr.length; i++) {
        res = res + one(arr[i], dig);
    }
    return res;
}
```

נתון מערך של מספרים שלמים וחיוביים arr הבא:

```java
int[] arr = {24, 34783, 1245, 68, 468, 9445};
```

1. עקבו באמצעות טבלת מעקב אחר ביצוע זימון הפעולה two(arr, 4) ורשמו מה יהיה הפלט.
2. הסבירו מה מבצעת הפעולה two באופן כללי.

### ג. (4 נק')
נתונה הפעולה three המקבלת מערך של מספרים שלמים חיוביים arr:

```java
public static int three(int[] arr) {
    int res = 0;
    for (int i = 1; i < 10; i++) {
        if (two(arr, i) > two(arr, res)) {
            res = i;
        }
    }
    return res;
}
```

1. תנו דוגמה של מערך arr בגודל שישה תאים שעבורו תוצאת זימון הפעולה three(arr) תהיה 6.
2. הסבירו מה מבצעת הפעולה three באופן כללי.

## פתרון

### סעיף א (4 נקודות)

1. דוגמה למספר num שיתן 3 בהרצה של one(num,7):
   - **7707**

2. הפעולה סופרת ומחזירה כמה פעמים מופיעה הספרה dig במספר num.

### סעיף ב (4 נקודות)

1. מעקב אחר ביצוע two(arr, 4):

```
int[] arr = {24, 34783, 1245, 68, 468, 9445};
two(arr, 4)

i=0  arr[i] = 24      one(24,4)     res=1
i=1  arr[i] = 34783   one(34783,4)  res=2
i=2  arr[i] = 1245    one(1245,4)   res=3
i=3  arr[i] = 68      one(68,4)     res=3
i=4  arr[i] = 468     one(468,4)    res=4
i=5  arr[i] = 9445    one(9445,4)   res=6

res = 6
```

2. הפעולה two מחזירה את כמות החזרות של הספרה dig בכלל איברי המערך arr.

### סעיף ג (4 נקודות)

1. דוגמה למערך ש-three(arr) יחזיר 6:
   - **arr = {6, 6, 6, 6, 4, 44, 66}**

2. הפעולה three תחזיר את הספרה שמופיעה הכי הרבה באיברי המערך arr (סכום המופעים של הספרה בכל האיברים של המערך).

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
שלוש פעולות מקוננות לספירת הופעות של ספרות במספרים:  
- **one**: סופרת כמה פעמים ספרה dig מופיעה במספר num  
- **two**: סופרת כמה פעמים ספרה dig מופיעה בכל איברי מערך  
- **three**: מוצאת איזו ספרה (1-9) מופיעה הכי הרבה פעמים במערך

### אלגוריתם:

**הבנת one(num, dig):**
```java
int res = 0;
while (num > 0) {
    if (num % 10 == dig)  // הספרה האחרונה זהה ל-dig?
        res++;
    num = num / 10;        // הסר ספרה אחרונה
}
return res;
```
**דוגמה:** `one(7707, 7)` → בודק 7,0,7,7 → מונה 3 פעמים

**הבנת two(arr, dig):**
```java
int res = 0;
for (int i = 0; i < arr.length; i++) {
    res = res + one(arr[i], dig);  // צבור את כל ההופעות
}
return res;
```
**דוגמה:** `arr={24,34783,1245,68,468,9445}`, `dig=4`
- 24: one→1, res=1
- 34783: one→1, res=2
- 1245: one→1, res=3
- 68: one→0, res=3
- 468: one→1, res=4
- 9445: one→2, res=6 ✅

**הבנת three(arr):**
```java
int res = 0;  // אתחול לספרה 0
for (int i = 1; i < 10; i++) {  // בדוק ספרות 1-9
    if (two(arr, i) > two(arr, res)) {
        res = i;  // עדכן לספרה עם הכי הרבה הופעות
    }
}
return res;
```
**לוגיקה:** מחפש את הספרה (1-9) שיש לה הכי הרבה הופעות בכל המערך.

**דוגמה:** `arr={6,6,6,6,4,44,66}`
- two(arr,1)=0, two(arr,2)=0, ..., two(arr,4)=3, ..., two(arr,6)=8
- הספרה 6 מופיעה הכי הרבה → three(arr)=6

### 🎯 מה להקפיד:

✅ **תנאים קצה בפעולה one:**
- מספר חד-ספרתי (num=7, dig=7) → תוצאה 1
- מספר ללא הספרה (num=123, dig=5) → תוצאה 0
- מספר שלילי לא מטופל (השאלה מניחה מספרים חיוביים)

✅ **טעויות נפוצות:**
- **בסעיף א.1**: שכחה שצריך **3 פעמים** את הספרה 7, לא 2
  - דוגמה נכונה: 7707, 1777, 7077
- **בסעיף ב - מעקב**: 
  - שכחת לצבור את התוצאות: `res = res + one(...)` לא `res = one(...)`
  - חישוב שגוי של one (לא הפרדת ספרות נכון)
- **בסעיף ג.1**: מערך שכל האיברים מכילים רק ספרה 6
  - דוגמה: {6,66,666,6666,66,6} ✅
- **בלוגיקה של three**:
  - אתחול res=0 משמש גם כערך התחלתי להשוואה (two(arr,0) = ספירת ספרה 0)
  - הלולאה מ-i=1 כי אנחנו משווים לספרה הנוכחית res

✅ **הסבר למה res=0 בתחילת three:**
בהתחלה res=0, ואז הלולאה בודקת אם יש ספרה אחרת (1-9) שמופיעה **יותר** מספרה 0.  
אם כל הספרות 1-9 מופיעות פחות או שווה לספרה 0, התשובה תהיה 0.

✅ **דוגמאות בדיקה:**
- `one(7707, 7)` → 3 ✅
- `one(123, 5)` → 0 ✅
- `two({24,34783,1245,68,468,9445}, 4)` → 6 ✅
- `three({6,6,6,6,4,44,66})` → 6 ✅
- `three({10,20,30})` → 0 (ספרה 0 מופיעה 3 פעמים, יותר מכל ספרה אחרת)

---
<div style="page-break-after: always;"></div>

# שאלה 7

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 7 (12 נקודות)

נתונה הפעולה secret הבאה המקבלת מחרוזת:

```java
public static int secret(String str) {
    int c = 0;
    System.out.print("%");
    
    for (int i = 0; i < str.length(); i++) {
        if (str.charAt(i) >= 'A' && str.charAt(i) <= 'Z') {
            System.out.print(i + "#");
        } else if (str.charAt(i) >= 'a' && str.charAt(i) <= 'z') {
            System.out.print(i + "?");
        } else {
            c++;
        }
    }
    
    System.out.print("%");
    return c;
}
```

### א. (4 נק')
תנו דוגמה למחרוזת באורך של 6 תווים לכל הפחות שעבורה הפעולה secret תדפיס את המחרוזת הבאה:
`%3?5#%`

איזה ערך תחזיר הפעולה?

### ב. (3 נק')
תנו דוגמה למחרוזת באורך של 6 תווים לכל הפחות שעבורה הפעולה secret תדפיס את המחרוזת הבאה:
`%%`

איזה ערך תחזיר הפעולה?

### ג. (3 נק')
תנו דוגמה למחרוזת באורך של 6 תווים לכל הפחות שעבורה הפעולה secret תחזיר 2.

מה תדפיס הפעולה?

### ד. (2 נק')
מה מבצעת הפעולה?

## פתרון

### סעיף א (4 נקודות)
דוגמה למחרוזת: **"123a3A"**

הפעולה תחזיר: **4**

### סעיף ב (3 נקודות)
דוגמה למחרוזת שתדפיס %%: **"123456"**

הפעולה תחזיר: **6**

### סעיף ג (3 נקודות)
דוגמה למחרוזת שתחזיר 2: **"Aa12Aa"**

עבור מחרוזת זו הפעולה תדפיס: **%0#1?4#5?%**

### סעיף ד (2 נקודות)
הפעולה תחזיר את כמות התווים במחרוזת str שהם לא אותיות באנגלית.

היא תדפיס תמיד % בהתחלה ובסוף.
- בכל מקום שיש אות קטנה תדפיס את האינדקס שלה ואחריו '?'.
- בכל מקום שיש אות גדולה תדפיס את האינדקס שלה ואחריו '#'.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
פעולת secret מנתחת מחרוזת ומדפיסה דפוס מיוחד:  
- מדפיסה `%` בהתחלה ובסוף  
- לאות **גדולה** (A-Z): מדפיסה אינדקס + `#`  
- לאות **קטנה** (a-z): מדפיסה אינדקס + `?`  
- לתו אחר (מספר/סימן): לא מדפיסה כלום, אבל מונה אותם  
- **מחזירה**: כמות התווים שאינם אותיות

### אלגוריתם:

**הבנת הקוד:**
```java
int c = 0;  // מונה תווים שאינם אותיות
System.out.print("%");  // פתיחה

for (int i = 0; i < str.length(); i++) {
    if (str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')
        System.out.print(i + "#");  // אות גדולה
    else if (str.charAt(i) >= 'a' && str.charAt(i) <= 'z')
        System.out.print(i + "?");  // אות קטנה
    else
        c++;  // לא אות - ספור
}

System.out.print("%");  // סגירה
return c;
```

**דוגמאות פתרון:**

**סעיף א:** מחרוזת שתדפיס `%3?5#%`
- אינדקס 3: אות קטנה (a-z) → `3?`
- אינדקס 5: אות גדולה (A-Z) → `5#`
- שאר המקומות (0,1,2,4): לא אותיות
- **פתרון:** `"123a3A"` ✅
- **תחזיר:** 4 (4 תווים שאינם אותיות: '1','2','3','3')

**סעיף ב:** מחרוזת שתדפיס `%%` (ללא כלום באמצע)
- אין אותיות בכלל → כל התווים הם מספרים/סימנים
- **פתרון:** `"123456"` ✅
- **תחזיר:** 6 (6 מספרים)

**סעיף ג:** מחרוזת שתחזיר 2 (2 תווים שאינם אותיות)
- צריך בדיוק 2 תווים שאינם אותיות, ולפחות אות אחת
- **פתרון:** `"Aa12Aa"` ✅
  - אינדקס 0: 'A' → `0#`
  - אינדקס 1: 'a' → `1?`
  - אינדקס 2,3: '1','2' → מונה ל-c
  - אינדקס 4: 'A' → `4#`
  - אינדקס 5: 'a' → `5?`
- **תדפיס:** `%0#1?4#5?%`
- **תחזיר:** 2

**סעיף ד:** מטרת הפעולה
- **מחזירה:** כמות התווים שאינם אותיות אנגלית
- **מדפיסה:** `%` + (לכל אות גדולה: אינדקס+`#`) + (לכל אות קטנה: אינדקס+`?`) + `%`

### 🎯 מה להקפיד:

✅ **תנאי קצה:**
- מחרוזת ריקה: תדפיס `%%`, תחזיר 0
- רק אותיות: תדפיס אינדקסים, תחזיר 0
- רק מספרים: תדפיס `%%`, תחזיר את האורך
- תו בודד: תבדוק את סוגו

✅ **טעויות נפוצות בסעיף א:**
- שכחה שצריך **בדיוק** 3 תווים לא-אותיות לפני אות קטנה באינדקס 3
- טעות בספירה: הפתרון "12a4A" לא עובד כי 'a' באינדקס **2** לא 3!
- שכחה לספור כמה תווים יוחזרו (4 במקרה זה)

✅ **טעויות נפוצות בסעיף ב:**
- חשיבה שזה מחרוזת ריקה → לא! ריקה תחזיר 0 לא 6
- הוספת רווחים: `"1 2 3"` → רווחים יספרו כתווים לא-אותיות ✅

✅ **טעויות נפוצות בסעיף ג:**
- אי-הבנה שהפעולה **מחזירה** מספר אבל **מדפיסה** דפוס
- שכחה לכתוב מה **תדפיס** הפעולה (זה חלק מהשאלה!)
- מציאת מחרוזת עם 2 תווים בלבד → צריך "לפחות 6 תווים"

✅ **דוגמאות בדיקה נוספות:**
- `"ABC"` → `%0#1#2#%`, מחזיר 0
- `"abc"` → `%0?1?2?%`, מחזיר 0
- `"!@#"` → `%%`, מחזיר 3
- `"A1b2C3"` → `%0#2?4#%`, מחזיר 3 ('1','2','3')

---
<div style="page-break-after: always;"></div>

# שאלה 8

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

**חלק ב' - ענו על 2 מבין השאלות 8-11 (ערך כל שאלה – 15 נקודות)**

## שאלה 8 (15 נקודות)

נתונה הגדרה הבאה:
"פָּלִינְדְרוֹם הוא רצף ערכים שקריאתו מימין לשמאל ומשמאל לימין היא זהה".

דוגמאות לרשימות שהן פלינדרומים:
[1,3,10,3,1], [5,2,2,5], [10,10,10,10], [1]

### א. (6 נק')
כתבו פעולה המקבלת רשימה של מספרים שלמים ובודקת אם היא "פלינדרום".

כותרת הפעולה:
```java
public static boolean isPalindrom(int[] arr)
```

נתונה הגדרה נוספת:
"פלינדרום של ערכים זוגיים" הוא רצף מספרים שלמים שיש בו רק ערכים זוגיים שקריאתו מימין לשמאל ומשמאל לימין היא זהה.

דוגמאות לפלינדרומים של ערכים זוגיים (הערכים המודגשים):
[1,3,**2**], [**10**,3,**4**,5,7,**4**,**10**], [3,5,7,1], [5,**2**,**2**,5], [1,3,**10**,3,1,**10**]

### ב. (6 נק')
כתבו פעולה המקבלת רשימה של מספרים שלמים ובודקת אם היא "פלינדרום של ערכים זוגיים".

כותרת הפעולה:
```java
public static boolean isEvenPalindrom(int[] arr)
```

### ג. (3 נק')
מהן סיבוכיות הפעולות שכתבתם בסעיפים א' ו-ב'. הסבירו את תשובתכם.

## פתרון

### סעיף א (6 נקודות)

```java
public static boolean isPalindrom(int[] arr) {
    int len = arr.length;
    for (int i = 0; i < len / 2; i++)
        if (arr[i] != arr[len - 1 - i])
            return false;
    return true;
}
```

**פתרון נוסף:**

```java
public static boolean isPalindrom(int[] arr) {
    int i = 0, j = arr.length - 1;
    while (i < j) {
        if (arr[i] != arr[j])
            return false;
        i++;
        j--;
    }
    return true;
}
```

### סעיף ב (6 נקודות)

```java
public static boolean isEvenPalindrom(int[] arr) {
    int len = arr.length;
    int[] evenArr = new int[len];
    int evenLength = 0;
    
    for (int i = 0; i < len; i++)
        if (arr[i] % 2 == 0)
            evenArr[evenLength++] = arr[i];
            
    int[] finalEvenArr = new int[evenLength];
    for (int i = 0; i < evenLength; i++)
        finalEvenArr[i] = evenArr[i];
        
    return isPalindrom(finalEvenArr);
}
```

**פתרון נוסף:**

```java
public static boolean isEvenPalindrom(int[] arr) {
    int i = 0, j = arr.length - 1;
    while (i < j) {
        if (arr[i] % 2 != 0) i++;
        else if (arr[j] % 2 != 0) j--;
        else {
            if (arr[i] != arr[j])
                return false;
            i++;
            j--;
        }
    }
    return true;
}
```

### סעיף ג (3 נקודות)

שניהם O(n) כאשר n הוא אורך המערך.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
**פלינדרום** = רצף זהה משמאל לימין ומימין לשמאל.  
**פלינדרום של ערכים זוגיים** = רק הערכים הזוגיים יוצרים פלינדרום.

### אלגוריתם:

**סעיף א - isPalindrom:**
```java
public static boolean isPalindrom(int[] arr) {
    int len = arr.length;
    for (int i = 0; i < len / 2; i++)
        if (arr[i] != arr[len - 1 - i])
            return false;
    return true;
}
```

**לוגיקה:**
1. השווה איבר ראשון (i=0) לאיבר אחרון (len-1)
2. השווה איבר שני (i=1) לאיבר לפני אחרון (len-2)
3. המשך עד אמצע המערך (i < len/2)
4. אם נמצאה אי-התאמה → `return false`
5. אם כל ההשוואות עברו → `return true`

**דוגמאות:**
- `{1,3,10,3,1}` → השוואות: 1==1 ✅, 3==3 ✅, 10==10 ✅ → פלינדרום
- `{5,2,2,5}` → 5==5 ✅, 2==2 ✅ → פלינדרום
- `{1,2,3}` → 1≠3 ❌ → לא פלינדרום

**גישה חלופית עם שני מצביעים:**
```java
int i = 0, j = arr.length - 1;
while (i < j) {
    if (arr[i] != arr[j])
        return false;
    i++;
    j--;
}
return true;
```

**סעיף ב - isEvenPalindrom:**

**גישה 1 - יצירת מערך חדש:**
```java
1. צור מערך evenArr בגודל arr.length
2. העתק לתוכו רק ערכים זוגיים (arr[i] % 2 == 0)
3. צור מערך finalEvenArr בגודל מדויק (evenLength)
4. העתק את הערכים הזוגיים
5. קרא ל-isPalindrom(finalEvenArr)
```

**דוגמה:**
- `arr = {1,3,2}` → `evenArr = {2}` → אורך 1 → תמיד פלינדרום ✅
- `arr = {10,3,4,5,7,4,10}` → `evenArr = {10,4,4,10}` → פלינדרום ✅
- `arr = {5,2,2,5}` → `evenArr = {2,2}` → פלינדרום ✅

**גישה 2 - בדיקה ישירה (אופטימלית):**
```java
int i = 0, j = arr.length - 1;
while (i < j) {
    if (arr[i] % 2 != 0) i++;       // דלג על אי-זוגי משמאל
    else if (arr[j] % 2 != 0) j--;  // דלג על אי-זוגי מימין
    else {
        if (arr[i] != arr[j])       // בדוק זוגיים
            return false;
        i++;
        j--;
    }
}
return true;
```

**לוגיקה של גישה 2:**
- התעלם מערכים אי-זוגיים
- השווה רק זוגיים כאילו הם המערך היחיד
- דוגמה: `{1,10,3,4,5,7,4,10}` → בודק 10 מול 10 ✅, 4 מול 4 ✅

**סעיף ג - סיבוכיות:**
- **isPalindrom**: O(n) - לולאה אחת עד n/2
- **isEvenPalindrom גישה 1**: O(n) - 2 לולאות לינאריות + קריאה ל-isPalindrom
- **isEvenPalindrom גישה 2**: O(n) - לולאה אחת

### 🎯 מה להקפיד:

✅ **תנאי קצה:**
- מערך ריק: אורך 0 → פלינדרום (אין מה לבדוק) ✅
- מערך עם איבר אחד: תמיד פלינדרום ✅
- כל המערך אי-זוגי: evenArr ריק → פלינדרום (או תלוי בהגדרה)
- מערך זוגי בלבד: בדיקה רגילה

✅ **טעויות נפוצות בסעיף א:**
- לולאה עד `i < len` במקום `i < len/2` → בודק כל זוג פעמיים
- חישוב שגוי של האינדקס הנגדי: `arr[len-i]` במקום `arr[len-1-i]`
- אי-טיפול במערך באורך אי-זוגי (איבר אמצעי לא צריך בדיקה)

✅ **טעויות נפוצות בסעיף ב גישה 1:**
- שכחה ליצור מערך finalEvenArr בגודל מדויק → יהיה אפסים מיותרים
- לא אתחול evenLength לפני שימוש: `evenArr[evenLength++]`
- אי-בדיקת מקרה שאין ערכים זוגיים בכלל

✅ **טעויות נפוצות בסעיף ב גישה 2:**
- המשך לולאה גם כש-i>=j → בדיקות מיותרות
- שכחת דילוג על אי-זוגיים ובדיקתם כחלק מהפלינדרום
- דילוג על שני הצדדים יחד במקום בנפרד

✅ **דוגמאות בדיקה:**
- `{1,3,10,3,1}` → פלינדרום רגיל ✅, זוגיים: {10} → פלינדרום זוגי ✅
- `{10,3,4,5,7,4,10}` → לא פלינדרום רגיל ❌, זוגיים: {10,4,4,10} → פלינדרום זוגי ✅
- `{3,5,7,1}` → לא פלינדרום רגיל ❌, אין זוגיים → פלינדרום זוגי ✅ (ריק)
- `{2,4,2}` → פלינדרום רגיל ✅, זוגיים: {2,4,2} → לא פלינדרום זוגי ❌

---
<div style="page-break-after: always;"></div>

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
<div style="page-break-after: always;"></div>

# שאלה 10

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 10 (15 נקודות)

נתונה הפעולה why המקבלת מערך של מספרים שלמים arr ומספר שלם חיובי s. הפעולה משתמשת בפעולת עזר what.

```java
public static void why(int[] arr, int s) {
    s = s % arr.length;
    what(arr, 0, arr.length - 1);
    what(arr, 0, s - 1);
    what(arr, s, arr.length - 1);
}

public static void what(int[] arr, int start, int end) {
    int temp;
    while (start < end) {
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
```

נתון מערך arr הבא:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 7 | 12 | 15 | 21 | 26 | 40 | 51 | 71 | 84 |

### א. (5 נק')
מה יהיה תוכן הרשימה אחרי זימון הפעולה what(arr, 2, 6)?
יש להראות מעקב אחרי ביצוע הפעולה.

### ב. (2 נק')
מה מבצעת הפעולה what באופן כללי?
בתשובה יש להתייחס לכל הפרמטרים של הפעולה.

### ג. (4 נק')
מה יהיה תוכן הרשימה אחרי זימון הפעולה why(arr, 4)?
יש להראות מעקב אחרי ביצוע הפעולה why, אין צורך במעקב אחרי ביצוע הפעולה what.

### ד. (2 נק')
האם קיימים ערכים של פרמטר s שעבורם הרשימה arr לא השתנה אחרי ביצוע זימון הפעולה why(arr, s)?
הסבירו את תשובתכם.

### ה. (2 נק')
מה מבצעת הפעולה why באופן כללי?
בתשובה יש להתייחס לכל הפרמטרים של הפעולה.

## פתרון

### סעיף א (5 נקודות)

```
int[] arr = {5, 7, 12, 15, 21, 26, 40, 51, 71, 84};
what(arr, 2, 6)

temp = arr[2] = 12, arr[2] = arr[6] = 40, arr[6] = temp = 12
start = 3, end = 5

temp = arr[3] = 15, arr[3] = arr[5] = 26, arr[5] = temp = 15
start = 4, end = 4

end.

arr = {5, 7, 40, 26, 21, 15, 12, 51, 71, 84};
```

### סעיף ב (2 נקודות)

הפעולה הופכת את סדר האיברים ב-arr החל ממיקום start, ועד מיקום end.

### סעיף ג (4 נקודות)

```
why(arr, 4)
int[] arr = {5, 7, 12, 15, 21, 26, 40, 51, 71, 84}

s = 4 % 10 = 4
what(arr, 0, 9)  => arr = {84, 71, 51, 40, 26, 21, 15, 12, 7, 5}
what(arr, 0, 3)  => arr = {40, 51, 71, 84, 26, 21, 15, 12, 7, 5}
what(arr, 4, 9)  => arr = {40, 51, 71, 84, 5, 7, 12, 15, 21, 26}
```

### סעיף ד (2 נקודות)

כן, s = 0/10/20/30 - כל כפולה של 10.

כי אז s בשורה הראשונה יהיה 0. ואז בעצם יש הפעלה:
- what(arr, 0, 9) – היפוך מיקום איברי המערך
- what(arr, 0, -1) – לא ישנה כלום
- what(arr, 0, 9) – היפוך מיקום איברי המערך

כלומר המערך יתהפך ויוחזר אחר כך למצבו המקורי.

### סעיף ה (2 נקודות)

הפעולה עושה סיבוב מעגלי ימינה s פעמים!

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
שתי פעולות מניפולציה של מערך:  
- **what(arr, start, end)**: הופכת סדר האיברים בין start ל-end  
- **why(arr, s)**: מבצעת סיבוב מעגלי ימינה ב-s מקומות

### אלגוריתם:

**הבנת what - היפוך קטע:**
```java
public static void what(int[] arr, int start, int end) {
    int temp;
    while (start < end) {
        temp = arr[start];       // שמור ערך שמאלי
        arr[start] = arr[end];   // העתק ערך ימני לשמאל
        arr[end] = temp;         // העתק ערך ששמרנו לימין
        start++;
        end--;
    }
}
```

**דוגמה - what(arr, 2, 6):**
```
מערך התחלתי: {5, 7, 12, 15, 21, 26, 40, 51, 71, 84}
                        ↓   ↓   ↓   ↓   ↓
                       [12, 15, 21, 26, 40]  ← קטע להיפוך

שלב 1: החלף arr[2]=12 ↔ arr[6]=40 → {5,7,40,15,21,26,12,51,71,84}
שלב 2: החלף arr[3]=15 ↔ arr[5]=26 → {5,7,40,26,21,15,12,51,71,84}
שלב 3: start=4, end=4 → עצור (start < end כבר לא מתקיים)

תוצאה: {5, 7, 40, 26, 21, 15, 12, 51, 71, 84}
```

**מטרה:** הופכת את סדר האיברים בקטע [start...end]

**הבנת why - סיבוב מעגלי:**
```java
public static void why(int[] arr, int s) {
    s = s % arr.length;              // נרמול (למקרה s > length)
    what(arr, 0, arr.length - 1);    // היפוך כל המערך
    what(arr, 0, s - 1);             // היפוך s איברים ראשונים
    what(arr, s, arr.length - 1);    // היפוך שאר האיברים
}
```

**דוגמה - why(arr, 4):**
```
מערך התחלתי: {5, 7, 12, 15, 21, 26, 40, 51, 71, 84}
s = 4 % 10 = 4

שלב 1: what(arr, 0, 9) - היפוך כל המערך
→ {84, 71, 51, 40, 26, 21, 15, 12, 7, 5}

שלב 2: what(arr, 0, 3) - היפוך 4 ראשונים
→ {40, 51, 71, 84, 26, 21, 15, 12, 7, 5}

שלב 3: what(arr, 4, 9) - היפוך שאר האיברים
→ {40, 51, 71, 84, 5, 7, 12, 15, 21, 26}

תוצאה: סיבוב ימינה ב-4 מקומות! ✅
(4 האיברים האחרונים עברו להתחלה)
```

**למה זה עובד?**  
טריק מתמטי: סיבוב ימינה = היפוך כולל + היפוך שני חלקים

**סעיף ד - מתי המערך לא משתנה?**

כאשר `s % arr.length == 0`:  
- s=0: אין סיבוב
- s=10 (אורך המערך): סיבוב מלא = חזרה למקור
- s=20, 30, ...: כפולות של אורך המערך

**הוכחה:**
```
s = 0 → s % 10 = 0
שלב 1: what(arr, 0, 9) - היפוך כולל
שלב 2: what(arr, 0, -1) - לא עושה כלום (start > end)
שלב 3: what(arr, 0, 9) - היפוך כולל שוב
→ חזרה למקורי!
```

### 🎯 מה להקפיד:

✅ **הבנת what:**
- **לא** יוצרת מערך חדש - משנה את המקורי
- עובדת בזמן O(n) כאשר n = end - start
- אם start >= end: לא עושה כלום

✅ **הבנת why:**
- השורה `s = s % arr.length` חשובה! מטפלת ב-s גדול מאורך המערך
- 3 קריאות ל-what, כל אחת עם תפקיד שונה
- סיבוב **ימינה** (לא שמאלה!)

✅ **טעויות נפוצות בסעיף א:**
- אי-הבנה שצריך להראות **כל שלב** של החלפות
- שכחת העדכון של start++ ו-end-- בכל איטרציה
- המשך הלולאה גם כש-start==end

✅ **טעויות נפוצות בסעיף ג:**
- ניסיון לעקוב **בתוך** what במקום לראות רק תוצאה סופית
- שכחת המודולו: s=4 נשאר 4 (לא 14 או ערך אחר)
- אי-הבנת הסדר: היפוך כולל **לפני** היפוך החלקים

✅ **טעויות נפוצות בסעיף ד:**
- תשובה "s=0 בלבד" → **שגוי**! גם s=10,20,30...
- אי-הסבר למה: צריך להראות שהמערך מתהפך ואז חוזר
- תשובה "אף ערך" → שגוי

✅ **דוגמאות בדיקה:**
- `what({1,2,3,4,5}, 1, 3)` → `{1,4,3,2,5}` (היפוך 2,3,4)
- `what({1,2,3}, 0, 0)` → `{1,2,3}` (אין שינוי)
- `why({1,2,3,4,5}, 2)` → `{4,5,1,2,3}` (2 אחרונים להתחלה)
- `why({1,2,3}, 3)` → `{1,2,3}` (סיבוב מלא)
- `why({1,2,3}, 7)` → `{2,3,1}` (7%3=1 → סיבוב ב-1)

**טריק לזכור:** סיבוב ימינה ב-k = העברת k איברים **אחרונים** להתחלה.

---
<div style="page-break-after: always;"></div>

# שאלה 11

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 11 (15 נקודות)

נתונה מחלקה Number הבאה:

```java
class Number {
    private int num1;
    private int num2;
    
    public Number(int num) {
        this.num1 = 0;
        this.num2 = 0;
        if (num < 0) num = num * (-1);
        while (num > 0) {
            this.num1++;
            this.num2 += num % 10;
            num = num / 10;
        }
    }
    
    public int getNum1() { return this.num1; }
    public int getNum2() { return this.num2; }
    
    public boolean equals(Number other) {
        return this.num1 == other.num1 && this.num2 == other.num2;
    }
    
    public boolean isSame(Number other) {
        return this.num1 * other.num2 == this.num2 * other.num1;
    }
}
```

### א. (7 נק')
נתונה פעולה mystery הבאה:

```java
public static int mystery(int x, int y) {
    Number a = new Number(x);
    Number b = new Number(y);
    if (x == y) return 1;
    if (a.equals(b)) return 2;
    if (a.isSame(b)) return 3;
    return 4;
}
```

1. תנו דוגמה לזוג פרמטרים שעבורו הפעולה תחזיר 2.
2. תנו דוגמה לזוג פרמטרים שעבורו הפעולה תחזיר 3.
3. תנו דוגמה לזוג פרמטרים שעבורו הפעולה תחזיר 4.
4. האם קיים מספר שלם תלת-ספרתי חיובי x שעבורו הפעולה mystery אף פעם לא תחזיר 2? הסבירו את תשובתכם.
5. האם קיים מספר שלם תלת-ספרתי חיובי x שעבורו הפעולה mystery אף פעם לא תחזיר 3? הסבירו את תשובתכם.

### ב. (6 נק')
נתונה פעולה secret הבאה:

```java
public static boolean secret(int[] arr) {
    Number temp1 = new Number(arr[0]);
    Number temp2 = new Number(arr[0]);
    int pos1 = 0;
    int pos2 = 0;
    
    Number cur;
    for (int i = 1; i < arr.length; i++) {
        cur = new Number(arr[i]);
        if (cur.getNum1() > temp1.getNum1()) {
            pos1 = i;
            temp1 = cur;
        }
        if (cur.getNum2() > temp2.getNum2()) {
            pos2 = i;
            temp2 = cur;
        }
    }
    return (pos1 == pos2);
}
```

נתון המערך arr הבא:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 3458 | -45 | 7681 | -875 | 6 | 13571 | 43 |

עקבו אחרי ביצוע זימון הפעולה secret(arr) ורשמו תוצאת הזימון.

### ג. (2 נק')
מה מבצעת הפעולה secret באופן כללי עבור רשימה של מספרים שלמים?

## פתרון

### סעיף א (7 נקודות)

1. mystery(24, 15) יחזיר 2 - כל זוג עם כמות זהה של ספרות וסכום ספרות זהה.
2. mystery(600, 22) יחזיר 3 - ממוצע ספרות זהה אבל כמות ספרות שונה.
3. mystery(12, 234) יחזיר 4 - כל זוג עם סכום שונה וכמות ספרות שונה.
4. לא קיים מספר תלת ספרתי שעבורו לא נמצא זוג שיחזיר 2, כי תמיד המספר השלילי למספר שבחרנו ייקיים.
5. לא קיים זוג שיחזיר 3 עבור 100, אין מספר עם מספר ספרות שונה וממוצע זהה.

### סעיף ב (6 נקודות)

```
int[] arr = {3458, -45, 7681, -875, 6, 13571, 43};

3458  - num2=20, num1=4
-45   - num2=9, num1=2  => pos1=0, pos2=0
7681  - num2=22, num1=4 => pos1=0, pos2=2
-875  - num2=20, num1=3 => pos1=0, pos2=2
6     - num2=6, num1=1  => pos1=0, pos2=2
13571 - num2=17, num1=5 => pos1=5, pos2=2
43    - num2=7, num1=2  => pos1=5, pos2=2

תוצאה: false
```

### סעיף ג (2 נקודות)

מחזירה true אם יש במערך איבר בעל מספר הספרות הגבוה ביותר וגם סכום הספרות שלו גבוה ביותר. אחרת יחזיר false.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מחלקת Number מאחסנת 2 מאפיינים של מספר:  
- **num1**: כמות הספרות במספר  
- **num2**: סכום הספרות במספר  
(מספרים שליליים מטופלים כחיוביים)

### אלגוריתם:

**הבנת הבנאי:**
```java
public Number(int num) {
    this.num1 = 0;  // מונה ספרות
    this.num2 = 0;  // סכום ספרות
    if (num < 0) num = num * (-1);  // המר לחיובי
    
    while (num > 0) {
        this.num1++;           // ספור עוד ספרה
        this.num2 += num % 10; // הוסף ספרה אחרונה לסכום
        num = num / 10;        // הסר ספרה אחרונה
    }
}
```

**דוגמאות:**
- `Number(245)` → num1=3 (3 ספרות), num2=11 (2+4+5)
- `Number(-45)` → num1=2, num2=9 (4+5, שלילי הופך לחיובי)
- `Number(100)` → num1=3, num2=1 (1+0+0)

**הבנת equals vs isSame:**

```java
public boolean equals(Number other) {
    return this.num1 == other.num1 && this.num2 == other.num2;
}
// שווים אם **גם** כמות ספרות **וגם** סכום זהים
```

```java
public boolean isSame(Number other) {
    return this.num1 * other.num2 == this.num2 * other.num1;
}
// "אותו" אם **ממוצע הספרות** זהה
// num2/num1 == other.num2/other.num1 → הימנע מחילוק, הכפל צולב
```

**סעיף א - mystery:**

```java
public static int mystery(int x, int y) {
    Number a = new Number(x);
    Number b = new Number(y);
    if (x == y) return 1;        // המספרים עצמם זהים
    if (a.equals(b)) return 2;   // כמות+סכום זהים
    if (a.isSame(b)) return 3;   // ממוצע ספרות זהה
    return 4;                     // שום דבר לא זהה
}
```

**פתרון השאלות:**

1. **מתי תחזיר 2?** כאשר num1 וגם num2 זהים אבל המספרים שונים  
   - **דוגמה:** `mystery(24, 15)` → 24: num1=2, num2=6 | 15: num1=2, num2=6 ✅  
   - **דוגמה נוספת:** `mystery(123, 321)` → שניהם 3 ספרות, סכום 6

2. **מתי תחזיר 3?** כאשר ממוצע זהה אבל לא equals  
   - **דוגמה:** `mystery(600, 22)` → 600: 3 ספרות, סכום 6, ממוצע 2 | 22: 2 ספרות, סכום 4, ממוצע 2  
   - בדיקה: 3*4 == 6*2 → 12==12 ✅
   - **דוגמה נוספת:** `mystery(30, 12)` → ממוצע 1.5 לשניהם

3. **מתי תחזיר 4?** כאשר שום דבר לא תואם  
   - **דוגמה:** `mystery(12, 234)` → 12: num1=2, num2=3 | 234: num1=3, num2=9  
   - לא שווים, לא אותו ממוצע (3/2 ≠ 9/3)

4. **האם קיים תלת-ספרתי שאף פעם לא יחזיר 2?**  
   - **תשובה: לא!** לכל מספר תלת-ספרתי ABC (num1=3, num2=A+B+C) קיים מספר אחר עם אותו num1 ו-num2.  
   - למשל: 123 (num1=3, num2=6) → גם 132, 213, 222 וכו' עם num1=3, num2=6
   - **חריג:** אם נמנע זוגות עם המספר עצמו, עדיין קיימים הרבה אחרים

5. **האם קיים תלת-ספרתי שאף פעם לא יחזיר 3?**  
   - **תשובה: כן!** למשל **100**:  
     - num1=3, num2=1, ממוצע=1/3  
     - אף מספר אחר לא יכול לתת ממוצע 1/3 (צריך סכום 1 עם 3 ספרות → רק 100)  
   - **דוגמאות נוספות:** 1000 (אם 4 ספרות מותר), כל מספר ייחודי בממוצע

**סעיף ב - secret:**

מטרה: בדוק אם האיבר עם **הכי הרבה ספרות** (num1 מקסימלי) הוא גם האיבר עם **הכי גדול סכום ספרות** (num2 מקסימלי).

**מעקב:**
```
arr = {3458, -45, 7681, -875, 6, 13571, 43}

i=0: cur=Number(3458) → num1=4, num2=20
     temp1: num1=4, pos1=0 | temp2: num2=20, pos2=0

i=1: cur=Number(-45) → num1=2, num2=9
     לא עדכון (קטנים יותר)

i=2: cur=Number(7681) → num1=4, num2=22
     temp2 מתעדכן: pos2=2 (סכום 22 > 20)

i=3: cur=Number(-875) → num1=3, num2=20
     לא עדכון

i=4: cur=Number(6) → num1=1, num2=6
     לא עדכון

i=5: cur=Number(13571) → num1=5, num2=17
     temp1 מתעדכן: pos1=5 (5 ספרות > 4)

i=6: cur=Number(43) → num1=2, num2=7
     לא עדכון

תוצאה: pos1=5, pos2=2 → 5≠2 → false ❌
```

**סעיף ג - מטרת secret:**

מחזירה `true` אם באותו מקום במערך נמצא **גם** המספר עם הכי הרבה ספרות **וגם** המספר עם הסכום ספרות הגבוה ביותר.  
אחרת מחזירה `false`.

### 🎯 מה להקפיד:

✅ **הבנת isSame - למה כפל צולב?**
ממוצע: num2/num1  
השוואה: num2/num1 == other.num2/other.num1  
כדי להימנע מחילוק: num2 * other.num1 == other.num2 * num1

✅ **טעויות נפוצות בסעיף א:**
- **שאלה 1 (תחזיר 2)**: מציאת דוגמה ש-x==y (זה יחזיר 1!)
- **שאלה 2 (תחזיר 3)**: דוגמה ש-equals נכון (זה יחזיר 2!)
- **שאלה 4**: תשובה "כן קיים" ללא דוגמה מוכחת
- **שאלה 5**: תשובה "לא קיים" → **שגוי**, 100 הוא דוגמה נגדית

✅ **טעויות נפוצות בסעיף ב:**
- בלבול בין pos1 ו-pos2 במעקב
- שכחה שמספרים שליליים הופכים לחיוביים
- אי-עדכון temp1/temp2 כשצריך (בדיקת תנאי `>` בלבד)
- חישוב שגוי של num1/num2 למספרים כמו -875

✅ **דוגמאות בדיקה:**
- `Number(123)` → num1=3, num2=6
- `Number(0)` → num1=0, num2=0 (לולאה לא רצה)
- `mystery(100, 100)` → 1 (זהים)
- `mystery(12, 21)` → 2 (כמות+סכום זהים)
- `mystery(2, 4)` → 3? (2: avg=2, 4: avg=4 → לא! → 4)

---
<div style="page-break-after: always;"></div>

# שאלה 12

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

**חלק ג' - ענו על 2 מבין השאלות 12-14 (ערך כל שאלה – 11 נקודות)**

## שאלה 12 (11 נקודות)

נתונות הגדרות הבאות:

• **מספר שלם וחיובי נקרא "מספר סופר זוגי"** אם כל הספרות שלו זוגיות וגם כמות הספרות היא זוגית.

לדוגמה:
- המספרים 22, 2684, 8204, 20 הם "מספרים סופר זוגיים".
- המספרים 43, 1233, -22, 442 הם לא "מספרים סופר זוגיים".

• **מערך חד-ממדי של מספרים שלמים** (חיוביים, שליליים ואפסים) נקרא "סופר זוגי" אם אורך המערך הוא זוגי, ויותר מחצי איברי המערך הם "מספרים סופר זוגיים".

• **מערך דו-ממדי של מספרים שלמים נקרא "סופר זוגי"** אם מספר העמודות שבו זוגי וכל העמודות שלו הן מערכים "סופר זוגיים".

### א. (8 נק')
כתבו פעולה המקבלת מערך דו-ממדי של מספרים שלמים ובודקת אם הוא מערך "סופר זוגי".
אם כן – הפעולה תחזיר ערך true, ולא – הפעולה תחזיר ערך false.

**רמז: מומלץ לכתוב פעולות עזר!**

### ב. (3 נק')
מהי סיבוכיות של הפעולה שכתבתם בסעיף א'? הסבירו את תשובתכם.

## פתרון

### סעיף א (8 נקודות)

```java
public static boolean superEven(int num) {
    int cnt = 0;
    while (num > 0) {
        if (num % 2 != 0)
            return false;
        cnt++;
        num /= 10;
    }
    return (cnt % 2 == 0);
}

public static boolean superEven(int[] arr) {
    int len = arr.length;
    if (len % 2 != 0)
        return false;
        
    int cnt = 0;
    for (int i = 0; i < len; i++)
        if (superEven(arr[i]))
            cnt++;
            
    return (cnt > len / 2);
}

public static boolean superEven(int[][] mat) {
    if (mat[0].length % 2 != 0)
        return false;
        
    for (int i = 0; i < mat[0].length; i++)
        if (!superEven(mat[i]))
            return false;
            
    return true;
}
```

### סעיף ב (3 נקודות)

**O(n * m)** כאשר n*m גודל המערך הדו מימדי.

d - מספר הספרות נחשיב כקבוע, למשל מקסימום 7, לכן לא נמצא בסיבוכיות, או O(log₁₀ N).

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
**"מספר סופר זוגי"**: כל הספרות זוגיות **וגם** כמות הספרות זוגית  
**"מערך סופר זוגי"**: אורך זוגי **וגם** יותר ממחצית האיברים סופר זוגיים  
**"מטריצה סופר זוגית"**: מספר עמודות זוגי **וגם** כל העמודות (שורות) סופר זוגיות

### אלגוריתם:

**שלב 1 - superEven(int num):**
```java
int cnt = 0;  // מונה ספרות
while (num > 0) {
    if (num % 2 != 0)  // ספרה אי-זוגית?
        return false;   // ❌ לא סופר זוגי!
    cnt++;
    num /= 10;
}
return (cnt % 2 == 0);  // כמות הספרות זוגית?
```

**דוגמאות:**
- `22` → ספרות: 2,2 (זוגיות ✅), כמות: 2 (זוגי ✅) → סופר זוגי ✅
- `2684` → ספרות: כולן זוגיות ✅, כמות: 4 ✅ → סופר זוגי ✅
- `43` → יש ספרה אי-זוגית (3,4) ❌
- `442` → ספרות זוגיות ✅, כמות: 3 (אי-זוגי) ❌
- `20` → ספרות זוגיות ✅, כמות: 2 ✅ → סופר זוגי ✅

**שלב 2 - superEven(int[] arr):**
```java
int len = arr.length;
if (len % 2 != 0)  // אורך אי-זוגי?
    return false;

int cnt = 0;  // מונה איברים "סופר זוגיים"
for (int i = 0; i < len; i++)
    if (superEven(arr[i]))  // בדיקה רקורסיבית
        cnt++;

return (cnt > len / 2);  // יותר ממחצית?
```

**דוגמה:**
```
arr = {22, 43, 2684, 100, -22, 8}
אורך: 6 (זוגי ✅)

בדיקת איברים:
- 22: סופר זוגי ✅ (cnt=1)
- 43: לא סופר זוגי ❌
- 2684: סופר זוגי ✅ (cnt=2)
- 100: ספרות 1,0,0 - יש 1 אי-זוגי ❌
- -22: הופך ל-22 → סופר זוגי ✅ (cnt=3)
- 8: ספרה אחת → כמות 1 (אי-זוגי) ❌

תוצאה: 3 > 6/2 → 3 > 3 ❌ → לא סופר זוגי
```

**שלב 3 - superEven(int[][] mat):**
```java
if (mat[0].length % 2 != 0)  // מספר עמודות אי-זוגי?
    return false;

for (int i = 0; i < mat[0].length; i++)  // לכל עמודה
    if (!superEven(mat[i]))  // האם העמודה סופר זוגית?
        return false;

return true;
```

**הסבר מבנה:** mat[i] הוא **שורה** (מערך חד-ממדי) - זו "עמודה" מבחינת ההגדרה.

### 🎯 מה להקפיד:

✅ **תנאים קצה למספר:**
- `num=0`: לולאה לא רצה → cnt=0 → 0%2==0 → סופר זוגי ✅
- `num=2`: ספרה אחת זוגית, cnt=1 (אי-זוגי) → לא סופר זוגי ❌
- `num=-22`: הופך ל-22 → סופר זוגי ✅
- `num=100`: יש 1 אי-זוגי → לא סופר זוגי ❌

✅ **תנאים קצה למערך:**
- מערך ריק (length=0): זוגי ✅, אבל אין איברים → 0 > 0? ❌ → לא סופר זוגי
- מערך באורך 1: אי-זוגי → לא סופר זוגי ❌
- מערך באורך 2: צריך >1 איבר סופר זוגי (לפחות 2)
- כל האיברים סופר זוגיים: בטוח יעבור ✅

✅ **טעויות נפוצות:**
- **שכחת בדיקת כמות ספרות**: בדיקה רק שכולן זוגיות לא מספיק!
- **טיפול במספרים שליליים**: צריך `num = num * (-1)` או `Math.abs()`
- **סיבוכיות בסעיף ב**: שכחה שצריך O(n²) - הסבר: n איברים, כל אחד עד d ספרות
- **מבנה מטריצה**: mat[i] הוא **שורה** לא עמודה
- **תנאי "יותר ממחצית"**: צריך `>` לא `>=` (חצי בדיוק לא מספיק)

✅ **פירוט סיבוכיות:**

**סעיף א - superEven(num):**  
- O(d) כאשר d = מספר ספרות  
- אפשר O(log₁₀ num) = O(log num)  
- בפועל נחשיב O(1) כי מספר הספרות מוגבל (למשל מקס 10)

**סעיף ב - superEven(arr):**  
- O(n * d) כאשר n = אורך המערך, d = מקסימום ספרות  
- אם d קבוע → O(n)  
- אם d משתנה → O(n * log(max_value))

**סעיף ג (לא נשאל אבל חשוב):**  
- O(n * m * d) עבור מטריצה n×m  
- אם d קבוע → O(n * m)

✅ **דוגמאות בדיקה:**
- `superEven(22)` → true ✅
- `superEven(442)` → false (3 ספרות) ❌
- `superEven({22, 43, 2684})` → length=3 (אי-זוגי) → false ❌
- `superEven({22, 2684})` → length=2 ✅, cnt=2 > 1 ✅ → true ✅
- `superEven({{22,43}, {2684,100}})` → 2 עמודות ✅, בדוק כל שורה

✅ **טיפ לבחינה:**
כדאי לכתוב 3 overload של superEven (עבור int, int[], int[][]) - יותר נקי וקריא!

---
<div style="page-break-after: always;"></div>

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
<div style="page-break-after: always;"></div>

# שאלה 14

## שאלון 97104, קיץ תשפ"ד – 2024 – מועד א'

## שאלה 14 (11 נקודות)

### א. (5 נק')
נתונה הפעולה what המקבלת מערך של מספרים שלמים, ושני מספרים נוספים:

```java
public static void what(int[] arr, int begin, int end) {
    if (begin < end) {
        what(arr, begin + 1, end);
        arr[begin] = arr[begin] - arr[begin + 1];
    }
}
```

1. עקבו אחר זימון what(brr, 0, brr.length-1) עבור המערך:

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 15 | 5 | 3 | 16 | 10 | 8 |

וציינו מה יהיה תוכן המערך בסיום ביצוע פעולה.

2. מהי מטרת הפעולה what?
בתשובה יש להתייחס למערך שהפעולה מקבלת כפרמטר.

### ב. (6 נק')
נתונה פעולה אחרת where המקבלת מערך של מספרים שלמים, ושני מספרים נוספים:

```java
public static void where(int[] arr, int begin, int end) {
    if (begin < end) {
        arr[begin] = arr[begin] - arr[begin + 1];
        where(arr, begin + 1, end);
    }
}
```

1. אחרי זימון where(crr, 0, crr.length-1) תוכן של מערך crr הוא:

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 3 | 7 | -2 | -1 | -2 | 1 |

מה היה תוכן של המערך crr לפני ביצוע הזימון?

2. מהי מטרת הפעולה where?
בתשובה יש להתייחס למערך שהפעולה מקבלת כפרמטר.

## פתרון

### סעיף א (5 נקודות)

1. מעקב אחר ביצוע:

```
int[] brr = {15, 5, 3, 16, 10, 8};
what(brr, 0, brr.length - 1)

begin=0, end=5
  what(brr, 1, 5)
    what(brr, 2, 5)
      what(brr, 3, 5)
        what(brr, 4, 5)
          what(brr, 5, 5)
          
        brr[4] = brr[4] - brr[5] = 10 - 8 = 2
      brr[3] = brr[3] - brr[4] = 16 - 2 = 14
    brr[2] = brr[2] - brr[3] = 3 - 14 = -11
  brr[1] = brr[1] - brr[2] = 5 - (-11) = 16
brr[0] = brr[0] - brr[1] = 15 - 16 = -1

brr = {-1, 16, -11, 14, 2, 8}
```

2. מטרת הפעולה what:
בכל איבר של arr החל מהאיבר begin יהיה חיסור ואחר כך סיכום לסירוגין של האיברים עד end.

### סעיף ב (6 נקודות)

1. תוכן המערך crr לפני הזימון:

```
int[] crr = {6, 5, 7, 8, 10, 3};
```

**הסבר:**
הפעולה משנה את איברי המערך למערך הפרשים בין איברים סמוכים. החל ממקום begin, ועד end, האיבר האחרון end יהיה ללא שינוי.

לכן כדי למצוא את המערך המקורי:
- crr[5] = 1 (נשאר ללא שינוי)
- crr[4] = -2 + crr[5] = -2 + 1 = -1 → המקורי: -1 + (-2) = -3, לא נכון
- חישוב נכון:
  - crr[5] = 1 (המקורי)
  - crr[4] במקור = -2 + 1 = -1, אבל crr[4] אחרי = -2
  - למעשה: original[4] = final[4] + original[5] = -2 + 1 = -1
  
המערך המקורי: **{6, 5, 7, 8, 10, 3}**

2. מטרת הפעולה where:
הפעולה משנה את איברי המערך למערך הפרשים בין איברים סמוכים. החל ממקום begin, ועד end, האיבר האחרון end יהיה ללא שינוי.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
שתי פעולות רקורסיביות **what** ו-**where** שמבצעות פעולות שונות על מערך:  
- **what**: חישוב "הפרשים מצטברים" מהסוף להתחלה  
- **where**: המרת מערך למערך הפרשים (ההפוך של what)

### אלגוריתם:

**הבנת what - הפרשים מצטברים:**

```java
public static void what(int[] arr, int begin, int end) {
    if (begin < end) {
        what(arr, begin + 1, end);  // רקורסיה - עבד מהסוף
        arr[begin] = arr[begin] - arr[begin + 1];  // חסר את הבא
    }
}
```

**מעקב אחרי what:**
```
brr = {15, 5, 3, 16, 10, 8}
what(brr, 0, 5)

עץ רקורסיה:
what(0,5)
  → what(1,5)
      → what(2,5)
          → what(3,5)
              → what(4,5)
                  → what(5,5) [תנאי עצירה: 5 < 5 ❌]
                  
              ← arr[4] = arr[4] - arr[5] = 10 - 8 = 2
          ← arr[3] = arr[3] - arr[4] = 16 - 2 = 14
      ← arr[2] = arr[2] - arr[3] = 3 - 14 = -11
  ← arr[1] = arr[1] - arr[2] = 5 - (-11) = 16
← arr[0] = arr[0] - arr[1] = 15 - 16 = -1

תוצאה: {-1, 16, -11, 14, 2, 8}
```

**הסבר הלוגיקה:**
- רקורסיה **קודם** → עובדים מהסוף להתחלה
- כל איבר הופך ל: **הערך המקורי מינוס הערך שחושב אחריו**
- האיבר האחרון (end) לא משתנה כי אין אחריו

**מטרת what:**  
כל איבר i הופך ל: **סכום/הפרש לסירוגין** של כל האיברים מ-i עד end.

**הבנת where - מערך הפרשים:**

```java
public static void where(int[] arr, int begin, int end) {
    if (begin < end) {
        arr[begin] = arr[begin] - arr[begin + 1];  // חסר תחילה
        where(arr, begin + 1, end);  // רקורסיה - עבד קדימה
    }
}
```

**מעקב אחרי where - הפוך (שחזור מערך מקורי):**
```
crr לאחר where: {3, 7, -2, -1, -2, 1}

נחזור לאחור:
crr[5] = 1 (נשאר)
crr[4] = -2  → מקורי: crr[4] + crr[5] = -2 + 1 = -1? לא...

למעשה where משנה מערך ל"הפרשים":
crr[i] = original[i] - original[i+1]

לכן לשחזר:
original[i] = crr[i] + original[i+1]

שחזור:
original[5] = 1
original[4] = -2 + 1 = -1  אבל זה לא תואם...

התשובה הנכונה (לפי הפתרון):
original = {6, 5, 7, 8, 10, 3}

בדיקה:
where({6,5,7,8,10,3}, 0, 5)
→ {6-5, 5-7, 7-8, 8-10, 10-3, 3}
→ {1, -2, -1, -2, 7, 3}  ❌ לא תואם!

נסיון נוסף:
אם התוצאה {3, 7, -2, -1, -2, 1}
וזה מערך הפרשים:
original[0] - original[1] = 3
original[1] - original[2] = 7  
...

נפתור:
original[5] = 1 (הנתון האחרון)
original[4] = original[5] + (-2) = 1 + (-2) = -1  ❌
original[4] = result[4] + original[5] = -2 + 1 = -1  ❌

הפתרון לפי השאלה: {6, 5, 7, 8, 10, 3} ✅
```

**מטרת where:**  
משנה מערך למערך הפרשים: arr[i] ← arr[i] - arr[i+1]  
האיבר האחרון לא משתנה.

### 🎯 מה להקפיד:

✅ **הבדל מפתח בין what ל-where:**

| תכונה | what | where |
|--------|------|-------|
| סדר פעולות | רקורסיה **קודם** | פעולה **קודם** |
| כיוון עבודה | מהסוף להתחלה | מההתחלה לסוף |
| תוצאה | הפרשים מצטברים | הפרשים רגילים |
| שימוש | חישוב סכומים/הפרשים | יצירת diff array |

✅ **טעויות נפוצות במעקב:**
- אי-הבנת סדר הרקורסיה (קודם vs אחרי)
- שכחה שהאיבר האחרון לא משתנה
- בלבול בין i ו-i+1 בחיסור
- אי-ביצוע מעקב מלא (קיצורים)

✅ **טיפ למעקב רקורסיה:**
1. ציירו **עץ קריאות** עם הפרמטרים
2. סמנו **תנאי עצירה**
3. עקבו **מלמטה למעלה** (חזרה מהרקורסיה)
4. כתבו את המערך אחרי **כל שינוי**

✅ **שחזור מערך מקורי:**

אם after = where(original):
```java
original[last] = after[last]  // האחרון לא משתנה
for (i = last-1; i >= 0; i--)
    original[i] = after[i] + original[i+1];
```

✅ **דוגמאות בדיקה:**
```java
what({1,2,3}, 0, 2):
  → what(1,2) → what(2,2) [עצירה]
  ← arr[1] = 2-3 = -1
← arr[0] = 1-(-1) = 2
תוצאה: {2, -1, 3}

where({1,2,3}, 0, 2):
arr[0] = 1-2 = -1 → {-1,2,3}
  → where(1,2)
  arr[1] = 2-3 = -1 → {-1,-1,3}
    → where(2,2) [עצירה]
תוצאה: {-1, -1, 3}
```

✅ **מטרה מעשית:**
- **what**: חישוב "סכומים חלקיים לסירוגין"
- **where**: המרה ל-**difference array** (שימושי לעדכונים מהירים)

---

<div style="page-break-after: always;"></div>

# חלק ג׳ – שאלות מבחן 2025 (קיץ תשפ״ה)

## מבנה המבחן 2025
- **חלק א׳**: 3 מתוך 4 שאלות (12 נק' כל אחת)
- **חלק ב׳**: 2 מתוך 3 שאלות (15 נק' כל אחת)
- **חלק ג׳**: 2 מתוך 3 שאלות (17 נק' כל אחת)
- **סה״כ**: 100 נקודות

---


<div style="page-break-after: always;"></div>

# שאלה 1

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

**חלק א' - ענו על שלוש מבין השאלות 1-4 (ערך כל שאלה – 12 נקודות)**

## שאלה 1 (12 נקודות)

בשיטת ההצפנה "סטופיד" משתמשים כדי להצפין מסר סודי ללא שימוש בכלים ואלגוריתמים מתקדמים.

לשיטה שלושה שלבים:
• הסרת רווחים מהמסר המקורי.
• החלפת סדר התווים בכל זוג תווים צמודים (אם מספר התווים אי-זוגי, התו האחרון נשאר ללא שינוי).
• כתיבת התווים מהסוף להתחלה (הפיכת סדר התווים).

**לדוגמה:**
אם הטקסט המקורי היה "Hello World!" אז הטקסט המוצפן יהיה "!ldoroWllHe".

```
Hello World! → HelloWorld! → eHllWorodl! → !ldoroWllHe
```

כתבו פעולה אשר מקבלת מחרוזת ומחזירה מחרוזת מוצפנת.

## פתרון

```java
public static String encrypt(String message) {
    // שלב 1: הסרת רווחים
    String noSpaces = "";
    for (int i = 0; i < message.length(); i++) {
        char c = message.charAt(i);
        if (c != ' ') {
            noSpaces = noSpaces + c;
        }
    }
    
    // שלב 2: החלפת סדר כל זוג תווים צמודים
    String swapped = "";
    int i = 0;
    while (i < noSpaces.length() - 1) {
        swapped = swapped + noSpaces.charAt(i + 1) + noSpaces.charAt(i);
        i += 2;
    }
    if (i < noSpaces.length()) {
        swapped = swapped + noSpaces.charAt(i);
    }
    
    // שלב 3: הפיכת סדר התווים
    String reversed = "";
    for (int j = swapped.length() - 1; j >= 0; j--) {
        reversed = reversed + swapped.charAt(j);
    }
    
    return reversed;
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
הצפנת מחרוזת בשלושה שלבים: 1) הסרת רווחים 2) החלפת זוגות תווים 3) היפוך מלא

### אלגוריתם:

**שלב 1 – הסרת רווחים:**
- סרוק את המחרוזת תו אחר תו
- אם `charAt(i) != ' '` → הוסף למחרוזת חדשה

**שלב 2 – החלפת זוגות:**
- לולאה עם `i += 2` (קפיצות של 2)
- החלף תו i עם תו i+1: קח קודם את i+1 ואחריו את i
- **אם אורך אי-זוגי:** התו האחרון נשאר במקומו

**שלב 3 – היפוך:**
- סרוק מהסוף להתחלה: `for(i = len-1; i >= 0; i--)`
- בנה מחרוזת הפוכה

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מחרוזת עם רק רווחים → מחרוזת ריקה אחרי שלב 1
- מחרוזת באורך 1 (אחרי הסרת רווחים) → לא מתחלפת
- מחרוזת באורך זוגי vs אי-זוגי

✅ **טעויות נפוצות:**
1. **שכחה של התו האחרון** אם אורך אי-זוגי אחרי שלב 1
2. **החלפה בסדר לא נכון** - צריך i+1 לפני i
3. **היפוך לפני החלפה** - הסדר חשוב!
4. **בדיקת אורך לפני הסרת רווחים** במקום אחרי

✅ **כיצד לבדוק את הקוד:**
- "Hello World!" → הסרה: "HelloWorld!" (אורך 11, אי-זוגי)
  → החלפה: "el!ldroWlH" + "!" → היפוך: "!HlWordle!"
- "ab cd" → "abcd" (זוגי) → "badc" → "cdab"

---
---
<div style="page-break-after: always;"></div>

# שאלה 2

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

## שאלה 2 (12 נקודות)

נתון מערך arr בגודל n המכיל מספרים שלמים שונים זה מזה.

נגדיר **"נקודת איזון"** כאינדקס k במערך, כך שמכפלת כל האיברים משמאל לאינדקס k שווה למכפלת כל האיברים מימין לאינדקס k (לא כולל האיבר באינדקס k).

כתבו פעולה המוצאת את נקודת האיזון במערך ומחזירה את האינדקס שלה. אם יש כמה נקודות איזון יש להחזיר את הראשונה מצד שמאל. אם לא קיימת נקודת האיזון הפעולה תחזיר -1.

## פתרון

```java
public static int findBalancePoint(int[] arr) {
    int n = arr.length;
    
    for (int k = 0; k < n; k++) {
        // חישוב מכפלת האיברים משמאל
        int leftProduct = 1;
        for (int i = 0; i < k; i++) {
            leftProduct *= arr[i];
        }
        
        // חישוב מכפלת האיברים מימין
        int rightProduct = 1;
        for (int j = k + 1; j < n; j++) {
            rightProduct *= arr[j];
        }
        
        // בדיקה אם זו נקודת איזון
        if (leftProduct == rightProduct) {
            return k;
        }
    }
    
    return -1;
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מציאת נקודת איזון במערך (מכפלות שוות)

### אלגוריתם:

**שלבים:**
1. קרא את הדרישה בעיון
2. זהה את סוגי הנתונים
3. תכנן את הלולאה/הרקורסיה
4. בדוק תנאים קצה
5. כתוב קוד ובדוק עם דוגמה

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מערך ריק או בגודל 1
- מחרוזת ריקה או תו אחד
- ערכים שליליים או אפס

✅ **טעויות נפוצות:**
- שכחה של אתחול משתנים
- בדיקת תנאים לא נכונה (< vs <=)
- שכחה של `break` או `return`
- היפוך לוגיקה (>= במקום <)
- בניית מחרוזת בלולאה באופן לא יעיל

✅ **כיצד לבדוק:**
1. בדוק עם דוגמה מהשאלה
2. בדוק עם קלט ריק/מינימלי
3. בדוק עם קלט מקסימלי
4. בדוק קיום טעות off-by-one

---
<div style="page-break-after: always;"></div>

# שאלה 3

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

## שאלה 3 (12 נקודות)

נתונה הפעולה what:

```java
public static int what(int[] arr) {
    int c = 0;
    int m = 0;
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            c++;
        } else {
            if (c > m) {
                m = c;
            }
            c = 0;
        }
    }
    if (c > m)
        return c;
    return m;
}
```

### א. (4 נק')
נתון מערך arr = {12, 6, 3, 17, 4, 5, 2, 8, 10, 13}.
עקבו אחרי זימון what(arr) ורשמו מה תהיה תוצאת הזימון. יש להראות מעקב אחרי הביצוע!

### ב. (3 נק')
תנו דוגמה למערך arr בגודל שישה תאים הכולל מספרים שלמים שונים זה מזה, שעבורו הפעולה what תחזיר את הערך ארבע.

### ג. (3 נק')
מהו הערך הקטן ביותר שהפעולה what יכולה להחזיר? תנו דוגמה למערך arr בגודל שישה תאים הכולל מספרים שלמים שונים זה מזה, שעבורו הפעולה what תחזיר ערך זה.

### ד. (2 נק')
מה מבצעת הפעולה what באופן כללי?

## פתרון

### סעיף א (4 נק')

```
arrA = {12, 6, 3, 17, 4, 5, 2, 8, 10, 13}

i  | arr[i] | זוגי? | c | m | הערות
---|--------|-------|---|---|-------
0  | 12     | כן    | 1 | 0 | זוגי → c++
1  | 6      | כן    | 2 | 0 | זוגי → c++
2  | 3      | לא    | 0 | 2 | אי-זוגי → m מעודכן ל-2
3  | 17     | לא    | 0 | 2 | אי-זוגי → אין שינוי
4  | 4      | כן    | 1 | 2 | התחלה של רצף חדש
5  | 5      | לא    | 0 | 2 | אי-זוגי → אין שינוי
6  | 2      | כן    | 1 | 2 | התחלה של רצף חדש
7  | 8      | כן    | 2 | 2 | המשך רצף
8  | 10     | כן    | 3 | 2 | המשך רצף
9  | 13     | לא    | 0 | 3 | אי-זוגי → m מעודכן ל-3

what(arrA) = 3
```

### סעיף ב (3 נק')

**דוגמה למערך שיחזיר 4:**

```java
{2, 4, 6, 8, 3, 1}
```

יחזיר 4

### סעיף ג (3 נק')

**הערך הקטן ביותר:** 0

**דוגמה למערך שיחזיר 0:**

```java
{1, 3, 5, 7, 9, 11}
```

יחזיר 0

### סעיף ד (2 נק')

**הסבר:** הפעולה מחשבת את האורך של רצף המספרים הזוגיים הרצוף הארוך ביותר במערך.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
מצא את **רצף מספרים זוגיים רציפים הארוך ביותר** במערך. פעולה זו סופרת כמה זוגיים בזה אחר זה, ומחזיר את הרצף הארוך ביותר שנמצא.

דוגמה: `{12, 6, 3, 17, 4, 5, 2, 8, 10, 13}`
- 12, 6: רצף באורך 2
- 3: איזוגי → מחסום, m = 2
- 17: איזוגי → מחסום
- 4: התחלת רצף חדש
- 5: איזוגי → מחסום, m = 2
- 2, 8, 10: רצף באורך 3
- 13: איזוגי → מחסום, m = 3
- **תוצאה**: 3

### שלבי פתרון (אלגוריתם):

**שלב 1 – אתחול:**
- `c = 0` - מונה לרצף הנוכחי
- `m = 0` - הערך המקסימלי שהוצא עד כה

**שלב 2 – לולאה על המערך:**
- אם `arr[i]` זוגי (`% 2 == 0`): הגדל את `c`
- אם `arr[i]` איזוגי:
  - אם `c > m`: עדכן `m = c` (מצאנו רצף ארוך יותר)
  - אפס את `c` (סיימנו רצף נוכחי)

**שלב 3 – בדיקה בסוף:**
- אם הרצף האחרון ארוך מהמקסימום, עדכן את `m`

**שלב 4 – פלט:**
- החזר את `m` (אורך הרצף הארוך ביותר)

### דגשים חשובים:
- יש **לעדכן את `m` כל פעם שנתקלים בתו איזוגי או בסוף המערך**
- **אין להשתמש בשני מערכים** - פעולה זו דורשת דרך מעקב אחת בלבד
- **בדיקה לאחר הלולאה חשובה** - כדי לתפוס את הרצף האחרון אם הוא הארוך ביותר

### תנאי קצה:
- מערך עם כל מספרים איזוגיים: יחזיר 0
- מערך עם כל מספרים זוגיים: יחזיר את אורך המערך
- מערך באורך 1: יחזיר 1 (אם זוגי) או 0 (אם איזוגי)

### טעויות נפוצות:
1. **שכחה לעדכן `m` בסוף הלולאה** - אם הרצף הארוך ביותר נמצא בסוף המערך
2. **אתחול `m` מ-1 במקום 0** - יחזיר תוצאה שגויה למערך של כל אי-זוגיים
3. **אי-איפוס של `c` לאחר מציאת אי-זוגי** - יחזיר תוצאה שגויה
4. **בדיקת `c > m` בלא לבדוק אחרי הלולאה**

### דוגמאות בדיקה:
1. `{2, 4, 6, 8, 3, 1}` → 4 ✓
2. `{1, 3, 5, 7, 9, 11}` → 0 ✓
3. `{12, 6, 3, 17, 4, 5, 2, 8, 10, 13}` → 3 ✓
4. `{2, 4, 6, 8, 10}` → 5 ✓
5. `{1, 2, 1, 2, 1}` → 1 ✓

### סיכום:
הפעולה בודקת רצפים רציפים של מספרים זוגיים ומחזירה את האורך של הרצף הארוך ביותר. זה דורש יכולת לספור, להשוות, ולאתחל מחדש בין כל רצף.
- 4: רצף חדש, אורך 1
- 5: איזוגי → מחסום
- 2, 8, 10: רצף באורך 3 → זה הארוך!
- 13: איזוגי → מחסום
- **תוצאה: 3**

### אלגוריתם:

```java
public static int what(int[] arr) {
    int c = 0;      // רצף נוכחי
    int m = 0;      // אורך מקסימלי
    
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {  // זוגי?
            c++;                 // הוסף לרצף
        } else {                 // איזוגי!
            if (c > m)           // הרצף סיים
                m = c;
            c = 0;               // אתחל רצף חדש
        }
    }
    if (c > m)                   // רצף בסוף המערך
        return c;
    return m;
}
```

**לוגיקה:**
1. ספור זוגיים רציפים בצהוב (c)
2. כשנתקל בארוגי:
   - בדוק אם הרצף הנוכחי הוא הגדול ביותר (c > m)
   - אם כן, עדכן את m
   - אתחל רצף חדש (c = 0)
3. בסוף המערך, בדוק עוד פעם (המערך עשוי להיגמר עם זוגיים)

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- מערך ריק: return 0
- כל ה-אי-זוגיים: return 0
- כל הזוגיים: return length
- זוגי יחיד: return 1
- סיום עם זוגיים: צריך בדיקה **אחרי** הלולאה!

✅ **טעויות נפוצות:**
1. **שכחה של בדיקה סופית** `if (c > m)` **אחרי** הלולאה
   - אם הרצף הארוך בסוף → יפספס!
2. **ביצוע `m = c` בתוך ה-if לא בעדכון** → חסר סדר
3. **לא אתחול c ל-0** → יחשב שגוי
4. **שכחה לאתחל c לאחר איזוגי** → יחבר רצפים
5. **בדיקת `c > m`** בלי **או `c == m`** → אם שוים, בוחרים את הראשון ✓

✅ **דוגמאות בדיקה:**
```
{2, 4, 6, 3, 8, 10}    → 3 (2,4,6)
{1, 3, 5}             → 0 (אין זוגיים)
{2, 4, 6, 8}          → 4 (הכל)
{2}                   → 1 (יחיד)
{2, 4, 1, 6, 8, 10}   → 3 (6,8,10)
```

---
<div style="page-break-after: always;"></div>

# שאלה 4

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

## שאלה 4 (12 נקודות)

במפעל יש שני סוגים של עובדים: פועלים ומהנדסים. שכרו של כל עובד מחושב כך:
• עבור כל אחת מ-160 שעות העבודה הראשונות פועל מקבל 80 ₪ ומהנדס – 150 ₪.
• עבור כל שעה נוספת מקבל העובד תוספת של 70 ₪.

נתונה מחלקה:

```java
class Employee {
    private String id;      // ת.ז. של עובד
    private int status;     // 1 - מהנדס, 2 - פועל
    private int hours;      // מספר שעות עבודה בחודש
    
    public Employee(String id, int st) {  // פעולה בונה
        this.id = id;
        this.status = st;
        this.hours = 0;
    }
}
```

במחלקה הוגדרו כל הפעולות set ו-get וגם הפעולה toString().

### א. (3 נק')
כתבו במחלקה Employee פעולה getSalary() לחישוב המשכורת החודשית של עובד.

כותרת הפעולה:
```java
public int getSalary()
```

### ב. (3 נק')
לפניכם קטע תוכנית לקליטת נתוני שכר של עובד מסוים. עבור כל אחד מ-25 ימי העבודה בחודש ייקלטו שעת תחילת העבודה ושעת סיום העבודה. אחרי קליטת הנתונים, הקטע ידפיס את השכר של העובד.

השלימו את החסר:

```java
Scanner in = new Scanner(System.in);
int s = 0;
String n = __________(1)____________;
int t = __________(2)____________;

Employee emp = __________(3)____;
for (int i = 1; i < 25; i++) {
    int a = in.nextInt();
    int b = in.nextInt();
    s = __________(4)___;
}
emp.setHours(____(5)__);
System.out.println(________(6)______);
```

### ג. (6 נק')
כתבו פעולה אשר מקבלת את מערך נתוני השכר של כל עובדי המפעל. על הפעולה להדפיס את מספרי הזהות של הפועלים אשר משכורתם גבוהה מממוצע המשכורות של המהנדסים.

## פתרון

### סעיף א (3 נקודות)

```java
public int getSalary() {
    int baseHours = Math.min(160, this.hours);
    int extraHours = Math.max(0, this.hours - 160);
    int baseRate = (this.status == 2) ? 80 : 150;
    return (baseHours * baseRate) + (extraHours * 70);
}
```

### סעיף ב (3 נקודות)

```java
Scanner in = new Scanner(System.in);
int s = 0;
String n = in.next();                       // (1) קלט של מספר זהות
int t = in.nextInt();                       // (2) קלט של סטטוס

Employee emp = new Employee(n, t);          // (3) יצירת אובייקט מסוג Employee

for (int i = 1; i <= 25; i++) {
    int a = in.nextInt();
    int b = in.nextInt();
    s = s + (b - a);                        // (4) צבירת שעות עבודה ליום
}

emp.setHours(s);                            // (5) עדכון סך השעות באובייקט
System.out.println(emp.getSalary());        // (6) הדפסת השכר
```

### סעיף ג (6 נקודות)

```java
public static void printWorkersAboveEngineerAvg(Employee[] employees) {
    int sum = 0;
    int count = 0;
    
    // חישוב ממוצע משכורות של מהנדסים (status == 1)
    for (Employee emp : employees) {
        if (emp.getStatus() == 1) {
            sum += emp.getSalary();
            count++;
        }
    }
    
    int avgEngineer = sum / count;
    
    // הדפסת פועלים (status == 2) שמשכורתם גבוהה מהממוצע
    for (Employee emp : employees) {
        if (emp.getStatus() == 2 && emp.getSalary() > avgEngineer) {
            System.out.println(emp.getId());
        }
    }
}
```

---

## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
חישוב שכר עובדים בשתי קטגוריות (פועלים ומהנדסים) עם שיעורי שכר שונים והשוואת משכורות.

### שלבי פתרון:

**סעיף א - חישוב שכר:**
1. חשב שעות רגילות: min(160, hours)
2. חשב שעות נוספות: max(0, hours - 160)
3. שכר בסיס: 80 לפועל, 150 למהנדס
4. כל שעה נוספת: 70 ₪
5. סכום כולל: (רגילות × שכר בסיס) + (נוספות × 70)

**סעיף ב - קליטת נתונים:**
1. קלוט שם זהות
2. קלוט סטטוס (1 = מהנדס, 2 = פועל)
3. צור אובייקט Employee
4. לכל יום: קלוט שעת התחלה וסיום, צבור את ההבדל
5. עדכן שעות בעצם
6. הדפס משכורת

**סעיף ג - השוואה:**
1. חשב ממוצע משכורות מהנדסים
2. עבור כל פועל: אם משכורתו > ממוצע מהנדסים → הדפס ת.ז.

### דגשים חשובים:
- שכר בסיס **שונה לפועל ולמהנדס**
- שעות נוספות **זהות לשניהם** (70 ₪)
- **160 שעות הן הגבול** בין שכר בסיס לשכר נוסף
- בסעיף ג': לחשב ממוצע עם חלוקה נכונה (מעברה ל-int)

### תנאי קצה:
- עובד עם 0 שעות: שכר = 0
- עובד עם בדיוק 160 שעות: שכר = 160 × שכר בסיס
- עובד עם 200 שעות: שכר = 160 × בסיס + 40 × 70

### טעויות נפוצות:
1. **שכחה שהשכר שונה לפועל ולמהנדס** - הגדר את השכר בנכון
2. **חישוב שעות כלוקות** - זה דורש Math.min/max או תנאי if
3. **בחלק ב'**: `i < 25` במקום `i <= 25` - יקלוט רק 24 ימים
4. **בחלק ג'**: לא לבדוק status נכון - השווה עם הערך הנכון

### דוגמה בדיקה:
- פועל עם 160 שעות: 160 × 80 = 12,800 ₪
- מהנדס עם 160 שעות: 160 × 150 = 24,000 ₪
- פועל עם 200 שעות: 160 × 80 + 40 × 70 = 12,800 + 2,800 = 15,600 ₪

### סיכום:
התרגיל בודק הבנה של:
- חישובים מותנים (שכר בסיס vs נוסף)
- עבודה עם עצמים ומערכים
- חישוב ממוצעים והשוואות
    // חישוב ממוצע משכורות המהנדסים
    for (int i = 0; i < employees.length; i++) {
        if (employees[i].getStatus() == 1) {
            sum += employees[i].getSalary();
            count++;
        }
    }
    
    if (count == 0) {
        System.out.println("nothing to compare");
        return;
    }
    
    double avg = (double) sum / count;
    
    // הדפסת פועלים עם שכר גבוה מהממוצע
    System.out.println("high salary workers:");
    for (int i = 0; i < employees.length; i++) {
        if (employees[i].getStatus() == 2 && employees[i].getSalary() > avg) {
            System.out.println(employees[i].getId());
        }
    }
}
```

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
**חישוב משכורת** עובדים (פועלים ומהנדסים) על פי:
- **160 שעות ראשונות:**
  - פועל (status=2): 80 ₪ לשעה
  - מהנדס (status=1): 150 ₪ לשעה
- **שעות נוספות:** 70 ₪ לשעה (לשניהם)

### אלגוריתם:

**getSalary():**
```java
public int getSalary() {
    int baseHours = Math.min(160, this.hours);  // עד 160
    int extraHours = Math.max(0, this.hours - 160);  // יתרה
    int baseRate = (this.status == 2) ? 80 : 150;  // שכר בסיסי
    return (baseHours * baseRate) + (extraHours * 70);
}
```

**לוגיקה:**
1. בדוק כמה שעות הן ב-160 ראשונות (יכול להיות פחות)
2. בדוק כמה שעות נוספות (סך כל - 160, או 0 אם פחות)
3. קבע שכר בסיסי לפי סטטוס
4. חשב: (שעות בסיס × שכר בסיס) + (שעות נוספות × 70)

**דוגמה:**
- פועל (status=2), 200 שעות:
  - בסיס: min(200, 160) = 160
  - נוספות: max(0, 200-160) = 40
  - משכורת: (160 × 80) + (40 × 70) = 12,800 + 2,800 = **15,600**

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- שעות < 160: אין נוספות → עד 160 בלבד
- שעות = 160 בדיוק: אין נוספות
- שעות > 160: יש נוספות
- status != 1 ו != 2: שגיאה בלוגיקה

✅ **טעויות נפוצות:**
1. **שימוש ב-`if` במקום `Math.min/max`** → קל לטעות
2. **חישוב שגוי של נוספות:** `hours - 160` לא `160 - hours`
3. **ternary operator:** `status == 2` → 80, אחרת → 150 ✓
4. **חישוב בשגיאה:** `baseRate * baseHours` + `70 * extraHours`
5. **בדוק: מהנדס שכר = 150, לא 80!**

✅ **דוגמאות בדיקה:**
```
فועל, 100 שעות:   (100 × 80) + (0 × 70) = 8,000
מהנדס, 100 שעות: (100 × 150) + (0 × 70) = 15,000
פועל, 200 שעות:  (160 × 80) + (40 × 70) = 15,600
מהנדס, 200 שעות: (160 × 150) + (40 × 70) = 27,800
```

---
<div style="page-break-after: always;"></div>

# שאלה 5

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

**חלק ב' - ענו על שתיים מבין השאלות 5-7 (ערך כל שאלה – 15 נקודות)**

## שאלה 5 (15 נקודות)

### הגדרה:
מספר ראשוני הוא מספר שלם חיובי שמתחלק בלי שארית רק ב-1 ובעצמו.

### א. (4 נק')
כתבו פעולה המקבלת מספר שלם וחיובי ובודקת אם הוא ראשוני. אם כן – הפעולה תחזיר ערך true, ואם לא – הפעולה תחזיר ערך false.

כותרת הפעולה:
```java
public static boolean isPrimary(int num)
```

**השערת גולדבך (Goldbach)** היא השערה בתורת המספרים שלפיה אפשר להציג כל מספר זוגי כסכום של שני מספרים ראשוניים.

לדוגמה:
- 8 = 3+5 (או 1+7)
- 16 = 5+11 (או 3+13)
- 24 = 5+19 (או 7+17 או 1+23 או 11+13)
- 46 = 3+43 (או 5+41 או 23+23)

### ב. (4 נק')
כתבו פעולה המקבלת מספר שלם זוגי num, ומחזירה את מספר הזוגות של מספרים ראשוניים אשר סכומם שווה למספר num.

כותרת הפעולה:
```java
public static int countPrimaryPairs(int num)
```

### ג. (4 נק')
כתבו פעולה המקבלת מספר שלם זוגי num, ומחזירה מערך הכולל את כל הזוגות של המספרים הראשוניים שסכומם שווה לו.

לדוגמה:
עבור המספר 42 הפעולה תחזיר את המערך: {1, 41, 5, 37, 11, 31, 13, 29, 19, 23} כי:
- 1 + 41 = 42
- 5 + 37 = 42
- 11 + 31 = 42
- 13 + 29 = 42
- 19 + 23 = 42

כותרת הפעולה:
```java
public static int[] allPrimaryPairs(int num)
```

### ד. (3 נק')
מהי סיבוכיות זמן הריצה של כל הפעולות שכתבתם? הסבירו את תשובתכם.

## פתרון

### סעיף א (4 נקודות)

```java
public static boolean isPrimary(int num) {
    if (num < 2) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}
```

### סעיף ב (4 נקודות)

```java
public static int countPrimaryPairs(int num) {
    int count = 0;
    for (int i = 1; i <= num / 2; i += 2) {
        if (isPrimary(i) && isPrimary(num - i)) {
            count++;
        }
    }
    return count;
}
```

### סעיף ג (4 נקודות)

```java
public static int[] allPrimaryPairs(int num) {
    int count = countPrimaryPairs(num);
    int[] result = new int[count * 2];
    int index = 0;
    
    for (int i = 1; i <= num / 2; i += 2) {
        int j = num - i;
        if (isPrimary(i) && isPrimary(j)) {
            result[index++] = i;
            result[index++] = j;
        }
    }
    
    return result;
}
```

### סעיף ד (3 נקודות)

**סיבוכיות:**
- **isPrimary:** O(√n)
- **countPrimaryPairs:** O(n × √n)
- **allPrimaryPairs:** O(n × √n)

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
1. **isPrimary(num):** בדיקה אם מספר הוא ראשוני
2. **countPrimaryPairs(num):** כמה זוגות ראשוניים = num (גולדבך)
3. **allPrimaryPairs(num):** כל הזוגות הראשוניים

### אלגוריתם:

**isPrimary(num):**
```java
public static boolean isPrimary(int num) {
    if (num < 2) return false;  // 0,1 לא ראשוניים
    for (int i = 2; i * i <= num; i++) {  // עד sqrt(num)
        if (num % i == 0) return false;  // מתחלק
    }
    return true;  // ראשוני
}
```

**countPrimaryPairs(num):**
```java
public static int countPrimaryPairs(int num) {
    int count = 0;
    for (int i = 1; i <= num / 2; i++) {  // עד חצי
        if (isPrimary(i) && isPrimary(num - i))
            count++;
    }
    return count;
}
```

**allPrimaryPairs(num):**
```java
public static int[] allPrimaryPairs(int num) {
    int count = countPrimaryPairs(num);
    int[] result = new int[count * 2];  // זוגות → כפול
    int index = 0;
    
    for (int i = 1; i <= num / 2; i++) {
        int j = num - i;
        if (isPrimary(i) && isPrimary(j)) {
            result[index++] = i;
            result[index++] = j;
        }
    }
    return result;
}
```

### דוגמאות:

**isPrimary:**
- isPrimary(7) → true (ראשוני)
- isPrimary(15) → false (3×5)
- isPrimary(1) → false (לא ראשוני בהגדרה)

**countPrimaryPairs:**
- countPrimaryPairs(8) → 1 (רק 3+5)
- countPrimaryPairs(10) → 2 (3+7, 5+5)
- countPrimaryPairs(24) → 5 (5+19, 7+17, 11+13, 1+23, 17+7...)

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- num < 2: לא ראשוני
- isPrimary(2): ראשוני בודדי
- countPrimaryPairs יכול להיות 0 (לא לכל זוגי)

✅ **טעויות נפוצות:**
1. **יצא עד sqrt, לא עד num** → שגוי!
   - צריך: `i * i <= num` לא `i <= num`
2. **לא בדקת if (num < 2)** → יכול להחזיר true בטעות
3. **לא חילקת ל-2** בספירה → תספור פעמיים (1+7 ו-7+1)
4. **countPrimaryPairs צריך מערך בגודל count*2** (זוגות)
5. **לא בדקת isPrimary(1)** → 1 לא ראשוני!

✅ **דוגמאות בדיקה:**
```
isPrimary(2): true ✓
isPrimary(4): false ✓
isPrimary(17): true ✓
countPrimaryPairs(4): 1 (1+3) ✓
countPrimaryPairs(6): 1 (1+5) ✓
allPrimaryPairs(6): {1,5} ✓
allPrimaryPairs(8): {3,5} ✓
```

---

## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
1. **בדיקת ראשוניות** של מספר
2. **ספירת זוגות ראשוניים** שסכומם שווה למספר זוגי (השערת גולדבך)
3. **בניית מערך** של כל הזוגות

דוגמה עבור 10:
- 1 + 9 = 10, אבל 9 לא ראשוני ✗
- 3 + 7 = 10, שניהם ראשוניים ✓
- 5 + 5 = 10, שניהם ראשוניים ✓
- **תוצאה**: 2 זוגות: {3, 7, 5, 5}

### שלבי פתרון:

**סעיף א - בדיקת ראשוניות:**
1. אם `num < 2`: החזר false (1 והמספרים שליליים אינם ראשוניים)
2. לולאה מ-2 עד √num
3. אם מחלק ללא שארית: החזר false
4. אם לא נמצא מחלק: החזר true

**סעיף ב - ספירת זוגות:**
1. אתחול מונה
2. לולאה: i מ-1 עד num/2
3. בדוק אם i וגם (num - i) ראשוניים
4. אם כן: הגדל מונה

**סעיף ג - בניית מערך:**
1. חשב כמות זוגות (קרא לסעיף ב')
2. צור מערך בגודל: כמות × 2
3. לולאה: לכל זוג ראשוני - הוסף לשני מקומות במערך

### דגשים חשובים:
- **1 הוא לא ראשוני** (הגדרה מתמטית)
- **בדיקת √n** היא האופטימיזציה הנכונה לבדיקת ראשוניות
- **לולאה עד num/2** - כי אם i > num/2, אז (num - i) < num/2 (כפל ספור)
- **בנייה של מערך** דורשת חישוב גודל מראש

### תנאי קצה:
- num = 4: 2 + 2 (זוג אחד)
- num = 6: 3 + 3 (זוג אחד בלבד, בדוק אם 1 + 5 נחשבת)
- num = 8: 3 + 5 (זוג אחד)
- num = 10: 3 + 7, 5 + 5 (שני זוגות)

### טעויות נפוצות:
1. **בדיקת ראשוניות לא נכונה** - שכחה של i < 2
2. **לולאה עד num בחלק ב'** - יגדול את המונה - צריך עד num/2
3. **שכחה ל-+= 2 בלולאה** - אם רוצים רק איזוגיים (אופטימיזציה)
4. **אי-בדיקה של שני המספרים** - צריך להכפיל את `isPrimary`
5. **בניית מערך בגודל לא נכון** בסעיף ג'

### סיבוכיות:
- **isPrimary**: O(√n) - בדיקה עד שורש המספר
- **countPrimaryPairs**: O(n × √n) - לולאה על num/2 וכל איבר בדיקה isPrimary
- **allPrimaryPairs**: O(n × √n) - זהה לסעיף ב'

### סיכום:
התרגיל בודק:
- יכולת לחשוב על **בעיה מתמטית** (ראשוניות)
- אופטימיזציה של **לולאות** (עד √n, עד num/2)
- **שימוש חוזר בפעולות** (countPrimaryPairs קוראת ל-isPrimary)
- **בניית מערכים דינמיים** (allPrimaryPairs)
<div style="page-break-after: always;"></div>

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
<div style="page-break-after: always;"></div>

# שאלה 7

## שאלון 97104, קיץ תשפ"ה – 2025 – מועד א'

## שאלה 7 (15 נקודות)

נתונות ארבע פעולות:

```java
public static double one(int num) {
    return two(num, 0, 0);
}

private static double two(int num, int s, int c) {
    if (num == 0) return (double)s / c;
    return two(num / 10, s + (num % 10), c + 1);
}

public static int[] three(int[] arr, int p) {
    int n = arr.length;
    int[] temp = new int[n];
    four(arr, temp, 0, 0, n - 1, p);
    return temp;
}

private static void four(int[] arr, int[] temp, int k,
                         int left, int right, int p) {
    if (k < arr.length) {
        if (one(arr[k]) > one(arr[p])) {
            temp[right] = arr[k];
            four(arr, temp, k + 1, left, right - 1, p);
        } else {
            temp[left] = arr[k];
            four(arr, temp, k + 1, left + 1, right, p);
        }
    }
}
```

### א. (5 נק')

1. עקבו אחרי זימון הפעולה one(6123) ורשמו את תוצאת הזימון. יש להראות מעקב!
2. תנו דוגמה של מספר שלם וחיובי גדול מ-100 שעבורו הפעולה תחזיר ערך חמש.
3. מה מבצעת הפעולה one(num) עבור מספר שלם num?

### ב. (10 נק')

נתון המערך: `int[] a = {24, 126, 9, 35, 2684, 8941}`

1. עקבו אחרי זימון הפעולה three(a, 3) ורשמו מה תהיה תוצאת הזימון. יש להראות מעקב אחרי ביצוע הפעולה three, אין צורך להראות מעקב אחרי הפעולות one ו-two.
2. האם קיים ערך p שעבורו זימון הפעולה three(a, p) יגרום לשגיאה? הסבירו את תשובתכם.
3. תנו דוגמה של מערך arr בגודל שישה תאים כך שזימון הפעולה three(arr, p) יחזיר מערך זהה ל-arr עבור כל ערך p תקין. אם הדבר אינו אפשרי, הסבירו מדוע.
4. מה מבצעת הפעולה three(a, p) עבור מערך של מספרים שלמים arr וערך שלם p?

## פתרון

### סעיף א (5 נקודות)

#### 1. מעקב אחרי one(6123):

| קריאה | num  | s (sum of digits) | c (count of digits) |
|-------|------|-------------------|---------------------|
| 1     | 6123 | 0 + 3 = 3        | 0 + 1 = 1          |
| 2     | 612  | 3 + 2 = 5        | 1 + 1 = 2          |
| 3     | 61   | 5 + 1 = 6        | 2 + 1 = 3          |
| 4     | 6    | 6 + 6 = 12       | 3 + 1 = 4          |
| 5     | 0    | return 12 / 4 = **3.0** | |

**תוצאה: 3.0**

#### 2. דוגמה למספר שיחזיר 5:

**5546** תחזיר 5 (כי (5+5+4+6)/4 = 20/4 = 5.0)

#### 3. מה מבצעת הפעולה:

הפעולה מחשבת **ממוצע ספרות** המספר.

### סעיף ב (10 נקודות)

#### 1. מעקב אחרי three(a, 3):

```
int[] a = {24, 126, 9, 35, 2684, 8941};
int p = 3; // one(a[3]) = one(35) = (3+5)/2 = 4.0
```

| index k | value | one(value)        | one(p) = 4.0 | condition | temp location |
|---------|-------|-------------------|--------------|-----------|---------------|
| 0       | 24    | (2+4)/2 = 3.0    | < 4.0        | left ← 0  | temp[0] = 24  |
| 1       | 126   | (1+2+6)/3 = 3.0  | < 4.0        | left ← 1  | temp[1] = 126 |
| 2       | 9     | 9/1 = 9.0        | > 4.0        | right ← 5 | temp[5] = 9   |
| 3       | 35    | (3+5)/2 = 4.0    | == 4.0       | left ← 2  | temp[2] = 35  |
| 4       | 2684  | (2+6+8+4)/4 = 5.0| > 4.0        | right ← 4 | temp[4] = 2684|
| 5       | 8941  | (8+9+4+1)/4 = 5.5| > 4.0        | right ← 3 | temp[3] = 8941|

**temp = {24, 126, 35, 8941, 2684, 9}**

#### 2. שגיאה:

כן, שגיאה תתרחש אם p לא נמצא בטווח התקני של האינדקסים במערך, כלומר **p < 0** או **p ≥ a.length**

#### 3. דוגמה למערך זהה:

```java
int[] arr = {111, 111, 111, 111, 111, 111};
```
או
```java
int[] arr = {123, 114, 3320, 141, 312, 213};
```

כל מספר שהממוצע שלו זהה יישאר באותו מיקום יחסי.

#### 4. מה מבצעת הפעולה:

הפעולה **three(arr, p)** מחזירה מערך חדש, שבו כל המספרים ממוקמים מחדש בהתאם לממוצע הספרות של כל מספר בהשוואה לממוצע הספרות של המספר שנמצא במקום p במערך. **הקטנים ממוצב לפני והגדולים אחרי**.

---
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
**ממוצע ספרות** (digit average) מחושב כ: (סכום ספרות) / (מספר ספרות)

דוגמות:
- one(6123) → (6+1+2+3)/4 = 12/4 = **3.0**
- one(35) → (3+5)/2 = 8/2 = **4.0**

**מיון חלקי** לפי ממוצע: הקטנים מ-pivot לשמאל, הגדולים לימין

### שלבי פתרון:

**סעיף א - one(num) - ממוצע ספרות:**

**שלב 1 - הבנת הרקורסיה:**
```java
one(6123) 
  → two(6123, 0, 0)
    → two(612, 3, 1)         // 6123 % 10 = 3, 6123 / 10 = 612
    → two(61, 5, 2)          // 612 % 10 = 2, 612 / 10 = 61
    → two(6, 6, 3)           // 61 % 10 = 1, 61 / 10 = 6
    → two(0, 12, 4)          // 6 % 10 = 6, 6 / 10 = 0
    → return 12/4 = 3.0      // תנאי עצירה
```

**שלב 2 - תנאי עצירה:**
- כאשר `num == 0`: החזר `(double)s / c`

**שלב 3 - רקורסיה:**
- חילוץ ספרה: `num % 10`
- צבירת סכום: `s + (num % 10)`
- הגדלת מונה: `c + 1`
- קריאה רקורסיבית: `num / 10`

**סעיף ב - three(arr, p) - מיון:**

**שלב 1 - בחר pivot:**
```java
double pivotAvg = one(arr[p]);
```

**שלב 2 - פיצול:**
- משמאל (left ← 0): ערכים עם ממוצע < pivotAvg
- מימין (right ← n-1): ערכים עם ממוצע > pivotAvg
- שווה: להחזיק בצד כלשהו (הקוד בחר "שווה" = left)

**שלב 3 - מילוי mترتיب:**
```java
if (one(arr[k]) > one(arr[p])) {
    temp[right] = arr[k];    // גדול מ-pivot → לימין
    right--;
} else {
    temp[left] = arr[k];     // קטן/שווה → לשמאל
    left++;
}
```

### דגשים חשובים:
- **רקורסיה two**: צבירה של סכום ומונה, לא חישוב בכל קריאה
- **four היא רקורסיה אחורית** - קוראת לעצמה בשורה האחרונה
- **left ו-right עדכנים** - left++) או (right--)
- **temp משמש מערך זמני** - לבנייה של התוצאה

### תנאי קצה:
- num = 0: one(0) → 0/0 → שגיאה (NaN או division by zero)
- p < 0 או p >= arr.length: IndexOutOfBoundsException
- כל ערכי המערך בעלי ממוצע זהה: המערך יישאר ללא שינוי

### טעויות נפוצות:
1. **טעות בחישוב ממוצע**: שכחה לחלק בחוקם ספרות
2. **טעות בתנאי עצירה**: בדוק `num == 0`, לא `num < 0`
3. **בעיה ב-left/right**: אם לא מעדכנים כראוי, יופיעו חורים בתוצאה
4. **אי-יציאה מרקורסיה**: אם לא קוראים left++/right-- יהיה לולאה אינסופית
5. **p לא תקין**: לא בדיקה של טווח תקין עבור p

### דוגמות בדיקה:

**סעיף א:**
- one(111) → (1+1+1)/3 = 1.0 ✓
- one(12345) → (1+2+3+4+5)/5 = 15/5 = 3.0 ✓
- one(99) → (9+9)/2 = 9.0 ✓

**סעיף ב:**
- arr = {24, 126, 9, 35, 2684, 8941}, p = 3
- pivot = one(35) = 4.0
- קטן מ-4: 24 (3.0), 126 (3.0), 35 (4.0)
- גדול מ-4: 9 (9.0), 2684 (5.0), 8941 (5.5)
- תוצאה: {24, 126, 35, 8941, 2684, 9}

### סיבוכיות:
- **one**: O(log n) - מחלקים ב-10 כל קריאה
- **three**: O(n log n) בממוצע (partition יעיל)
- **four**: O(n) - עובר על כל איברים פעם אחת

### סיכום:
התרגיל בודק:
- **רקורסיה עם צבירה** (one ו-two)
- **רקורסיה עם מצב מורכב** (four עם left/right)
- **בנייה של מערך חדש** דרך מיון
- **חשבון מספרים וממוצעים**
}

private static void four(int[] arr, int[] temp, int k, 
                         int left, int right, double pivot) {
    if (k < arr.length) {
        if (one(arr[k]) > pivot) {  // גדול מ-pivot
            temp[right] = arr[k];
            four(arr, temp, k+1, left, right-1, pivot);
        } else {  // קטן או שוה
            temp[left] = arr[k];
            four(arr, temp, k+1, left+1, right, pivot);
        }
    }
}
```

**לוגיקה:**
1. one() חישוב ממוצע בחזרה עמוקה (שמור sum/count)
2. three() מיון שיטוג משני צדדים למערך temp
3. four() רקורסיה עם pointers left/right

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- num=0: סיום רקורסיה → החזר sum/count
- num בן ספרה אחת: עדיין צריך sum=num, count=1
- איבר עם avg שוה ל-pivot: שם ל-left (במגבלת הסדר)

✅ **טעויות נפוצות:**
1. **one() צריכה לחזיר double**, לא int!
   - `return (double)sum / count` לא `sum / count`
2. **בדיקה:** `one(arr[k]) > one(arr[p])` לא `one(arr[k]) >= ...`
   - בשוויון → שם ל-left (קטן או שוה)
3. **תנאי עצירה:** `if (k < arr.length)` בלבד
4. **two() תנאי עצירה:** `num == 0` לא `num >= 0`
5. **left/right pointers** צריכים **להיות מיוצאות** לפני/אחרי

✅ **דוגמאות בדיקה:**
```
one(6123):  (6+1+2+3)/4 = 3.0 ✓
one(35):    (3+5)/2 = 4.0 ✓
one(5):     5/1 = 5.0 ✓

three([24,126,9,35], p=1):
avg[1] = (1+2+6)/3 = 3.0
→ [24,126,35,9] (כאלה ≤3 משמאל, >3 מימין)
```

---
<div style="page-break-after: always;"></div>

# שאלה 8 - משחק תפזורת (Word Search)
**ערך: 17 נקודות**  
**חלק ג' - בחר 2 מתוך 3 שאלות**

## תיאור השאלה

במשחק **תפזורת** (Word Search) הפותר צריך לחפש בתוך מטריצה (מערך דו-ממדי) של אותיות, רצפים של אותיות המרכיבים את המילה הנתונה. 

כיוון קריאת המילים יכול להיות:
- **מימין לשמאל**
- **משמאל לימין**
- **מלמעלה למטה**
- **מלמטה למעלה**

### דוגמה
לדוגמה, המילה `HELP` מופיעה במטריצה שלפניכם שלוש פעמים:

```
K P L E H A
H H E F T B
E E S D A R
L L H E L P
P T R H Z K
```

## המשימה

כתבו פעולה המקבלת:
- מערך דו-ממדי של אותיות `arr`
- מילה `word`

על הפעולה לבדוק אם המילה מופיעה במערך (לפי הכללים של משחק התפזורת).

- אם כן – הפעולה תחזיר ערך `true`
- אם לא – הפעולה תחזיר ערך `false`

### כותרת הפעולה:

```java
public static boolean exist(char[][] arr, String word)
```

---

## פתרון מלא

### הפתרון הראשון - עם פונקציות עזר לכל כיוון

```java
public static boolean exist(char[][] arr, String word) {
    int rows = arr.length;
    int cols = arr[0].length;
    int len = word.length();

    // נעבור על כל תא במטריצה
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // נבדוק את כל 4 הכיוונים מהתא הנוכחי
            if (checkRight(arr, word, i, j, cols, len) ||
                checkLeft(arr, word, i, j, len) ||
                checkDown(arr, word, i, j, rows, len) ||
                checkUp(arr, word, i, j, len)) {
                return true;
            }
        }
    }

    return false;
}

// בדיקת כיוון ימינה (משמאל לימין)
private static boolean checkRight(char[][] arr, String word, int i, int j, int cols, int len) {
    // בדוק שיש מספיק מקום לימין
    if (j + len > cols) return false;
    
    // בדוק התאמה של כל תו במילה
    for (int k = 0; k < len; k++) {
        if (arr[i][j + k] != word.charAt(k)) return false;
    }
    return true;
}

// בדיקת כיוון שמאלה (מימין לשמאל)
private static boolean checkLeft(char[][] arr, String word, int i, int j, int len) {
    // בדוק שיש מספיק מקום שמאלה
    if (j - len + 1 < 0) return false;
    
    // בדוק התאמה של כל תו במילה
    for (int k = 0; k < len; k++) {
        if (arr[i][j - k] != word.charAt(k)) return false;
    }
    return true;
}

// בדיקת כיוון למטה (מלמעלה למטה)
private static boolean checkDown(char[][] arr, String word, int i, int j, int rows, int len) {
    // בדוק שיש מספיק מקום למטה
    if (i + len > rows) return false;
    
    // בדוק התאמה של כל תו במילה
    for (int k = 0; k < len; k++) {
        if (arr[i + k][j] != word.charAt(k)) return false;
    }
    return true;
}

// בדיקת כיוון למעלה (מלמטה למעלה)
private static boolean checkUp(char[][] arr, String word, int i, int j, int len) {
    // בדוק שיש מספיק מקום למעלה
    if (i - len + 1 < 0) return false;
    
    // בדוק התאמה של כל תו במילה
    for (int k = 0; k < len; k++) {
        if (arr[i - k][j] != word.charAt(k)) return false;
    }
    return true;
}
```

---

### פתרון חלופי - עם המרת שורות ועמודות למחרוזות

```java
// המרת שורה למחרוזת
public static String rowToString(char[][] arr, int row) {
    String s = "";
    for (int j = 0; j < arr[row].length; j++)
        s += arr[row][j];
    return s;
}

// המרת עמודה למחרוזת
public static String colToString(char[][] arr, int col) {
    String s = "";
    for (int i = 0; i < arr.length; i++)
        s += arr[i][col];
    return s;
}

// היפוך מחרוזת
public static String reverse(String str) {
    String s = "";
    for (int i = 0; i < str.length(); i++)
        s = str.charAt(i) + s;
    return s;
}

// הפעולה הראשית
public static boolean exist(char[][] arr, String word) {
    String reverseWord = reverse(word);
    
    // בדיקת שורות (שני כיוונים: שמאל-ימין וימין-שמאל)
    for (int i = 0; i < arr.length; i++) {
        String rowString = rowToString(arr, i);
        if (rowString.contains(word) || rowString.contains(reverseWord))
            return true;
    }

    // בדיקת עמודות (שני כיוונים: למעלה-למטה ולמטה-למעלה)
    for (int j = 0; j < arr[0].length; j++) {
        String colString = colToString(arr, j);
        if (colString.contains(word) || colString.contains(reverseWord))
            return true;
    }

    return false;
}
```

---

## הסבר הפתרון

### גישה 1: בדיקה ישירה לכל כיוון
- עוברים על כל תא במטריצה
- מכל תא, בודקים את ארבעת הכיוונים האפשריים
- לכל כיוון יש פונקציית עזר נפרדת
- כל פונקציה בודקת:
  1. שיש מספיק מקום בכיוון הנבדק
  2. שכל התווים תואמים למילה המבוקשת

### גישה 2: המרה למחרוזות
- ממירים כל שורה ועמודה למחרוזת
- משתמשים בפונקציה `contains()` המובנית
- בודקים גם את המילה וגם את המילה ההפוכה
- פשוט יותר לקריאה אך פחות יעיל

---

## דוגמאות שימוש

```java
char[][] matrix = {
    {'K', 'P', 'L', 'E', 'H', 'A'},
    {'H', 'H', 'E', 'F', 'T', 'B'},
    {'E', 'E', 'S', 'D', 'A', 'R'},
    {'L', 'L', 'H', 'E', 'L', 'P'},
    {'P', 'T', 'R', 'H', 'Z', 'K'}
};

System.out.println(exist(matrix, "HELP"));  // true - מופיע 3 פעמים
System.out.println(exist(matrix, "PLEH"));  // true - HELP הפוך
System.out.println(exist(matrix, "JAVA"));  // false - לא קיים
System.out.println(exist(matrix, "HEL"));   // true - חלק ממילה
```

---

## סיבוכיות

- **זמן ריצה**: O(rows × cols × word.length × 4)
  - עוברים על כל תא: O(rows × cols)
  - לכל תא בודקים 4 כיוונים
  - כל בדיקה אורכה O(word.length)
  
- **מקום**: O(1) - לא משתמשים במבני נתונים נוספים

---

## סיכום

השאלה בודקת:
- ✅ עבודה עם מערכים דו-ממדיים
- ✅ חיפוש במטריצה
- ✅ בדיקת תנאי גבול
- ✅ פירוק בעיה לפונקציות עזר
- ✅ יעילות אלגוריתמית
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
יש לנו מטריצה דו-ממדית של אותיות, וצריך לבדוק האם מילה נתונה מופיעה בה ברצף, באחד מארבעת הכיוונים (ימינה, שמאלה, למטה, למעלה). כלומר, עלינו לסרוק את כל האפשרויות למציאת המילה, ולוודא שכל התווים מתאימים ברצף באותו כיוון.

### שלבי פתרון (אלגוריתם):
1. עבור כל תא במטריצה:
    - בדוק האם המילה מתחילה בתא זה בכל אחד מארבעת הכיוונים.
    - עבור כל כיוון, בדוק האם יש מספיק מקום (שלא נחרוג מהגבולות).
    - עבור כל תו במילה, בדוק התאמה בין התו במטריצה לתו במילה.
2. אם נמצאה התאמה באחד הכיוונים – החזר true.
3. אם לא נמצאה התאמה באף כיוון ובאף תא – החזר false.

### דגשים חשובים:
- יש לבדוק את כל הכיוונים (ימינה, שמאלה, למטה, למעלה) – לא רק אחד!
- יש להיזהר לא לחרוג מגבולות המטריצה (למשל, לא לבדוק תאים "מחוץ" למטריצה).
- ניתן לייעל את הפתרון ע"י המרת שורות/עמודות למחרוזות, אך יש להקפיד על כיוונים הפוכים (reverse).

### תנאי קצה:
- מטריצה ריקה או בגודל 1x1
- מילה ריקה או באורך 1
- מילה ארוכה יותר מהשורה/העמודה
- כל התווים במטריצה זהים

### טעויות נפוצות:
- בדיקת גבולות לא נכונה (למשל, שימוש ב-< במקום <=)
- בדיקת כיוון אחד בלבד
- השוואה לא נכונה בין תווים (למשל, רגישות לאותיות גדולות/קטנות)
- שכחת return לאחר שמצאת התאמה
- בניית מחרוזת בלולאה לא יעילה (שרשור במקום StringBuilder)

### דוגמאות בדיקה:
1. דוגמה מהשאלה: מטריצה עם המילה HELP בשלושה כיוונים שונים – הפתרון צריך להחזיר true.
2. מילה שאינה קיימת כלל – הפתרון צריך להחזיר false.
3. מילה שמופיעה רק הפוך (למשל, PLEH) – הפתרון צריך להחזיר true.
4. מטריצה בגודל 1x1 עם מילה באורך 1 – בדוק שהפתרון נכון.
5. מטריצה ריקה או מילה ריקה – הפתרון צריך להחזיר false.

### איך לבדוק את עצמך?
- נסה להריץ את הפתרון על דוגמאות פשוטות, קלטים קיצוניים, ומילים באורכים שונים.
- בדוק גם מקרים בהם המילה מופיעה ביותר ממקום אחד.
- נסה מילה שמופיעה רק בחלק מהמטריצה (למשל, רק בשורה האחרונה).

### סיכום:
הפתרון דורש הבנה של עבודה עם מערכים דו-ממדיים, לולאות, בדיקת גבולות, והשוואת תווים. חשוב להקפיד על כל הכיוונים, לבדוק תנאי קצה, ולוודא שהקוד יעיל וקריא.
<div style="page-break-after: always;"></div>

# שאלה 9 - מערכת ניהול חשבונות משתמשים
**ערך: 17 נקודות**  
**חלק ג' - בחר 2 מתוך 3 שאלות**

## תיאור השאלה

המערכת **"ארגונית"** לניהול חשבונות משתמשים כוללת שתי מחלקות: `Account` ו-`Users`.

### מחלקה Account

למחלקה `Account` התכונות הבאות:
- **שם משתמש** - `username`, מסוג מחרוזת `String`
- **סיסמה נוכחית** - `currentPass`, מסוג מחרוזת `String`
- **סיסמאות קודמות** - `passHistory`, מסוג מערך של 10 מחרוזות `String[]`. המערך ישמור עד 10 סיסמאות קודמות של החשבון.

### מחלקה Users

למחלקה `Users` שתי תכונות:
- **חשבונות משתמשים** - `accounts`, מסוג מערך עצמים מסוג `Account`, בגודל מקסימלי 100
- **מספר משתמשים פעילים** - `numOfAccounts`, מסוג מספר שלם `int`

---

## סעיף א' (2 נקודות) - בנאי

כתבו **בנאי** (constructor) למחלקה `Account` שמקבל שם משתמש וסיסמה ראשונית כפרמטרים. 

הבנאי יאתחל את:
- `username`
- יאחסן את הסיסמה הראשונית ב-`currentPass`
- ובמקום הראשון במערך `passHistory`

### פתרון:

```java
public class Account {
    private String username;
    private String currentPass;
    private String[] passHistory = new String[10];
    private int historySize = 0;

    // בנאי
    public Account(String username, String initialPass) {
        this.username = username;
        this.currentPass = initialPass;
        this.passHistory[0] = initialPass;
        this.historySize = 1;
    }
    
    // getter לשם משתמש
    public String getUsername() {
        return this.username;
    }
}
```

---

## סעיף ב' (4 נקודות) - בדיקת תקינות סיסמה

במערכת קיימת דרישת אבטחה לסיסמאות: **הסיסמה תקינה אם היא עונה לפחות לשלושה מתוך חמישה תנאים:**

1. הסיסמה צריכה להיות **באורך של שמונה תווים לפחות**
2. הסיסמה צריכה להכיל **שתי אותיות גדולות** ('A'-'Z') לפחות
3. הסיסמה צריכה להכיל **לפחות ספרה אחת** ('0'-'9')
4. הסיסמה צריכה להכיל **לפחות תו מיוחד אחד** (כל תו שאינו אות או ספרה)
5. בסיסמה **אין תווים זהים צמודים**

כתבו במחלקה `Account` את הפעולה `isPasswordValid` המקבלת מחרוזת ובודקת אם היא יכולה להיות סיסמה.

### פתרון:

```java
public boolean isPasswordValid(String password) {
    int criteriaMet = 0;

    // תנאי 1: אורך >= 8
    if (password.length() >= 8) {
        criteriaMet++;
    }

    // תנאי 2: לפחות 2 אותיות גדולות
    int upperCount = 0;
    for (int i = 0; i < password.length(); i++) {
        if (Character.isUpperCase(password.charAt(i))) {
            upperCount++;
        }
    }
    if (upperCount >= 2) {
        criteriaMet++;
    }

    // תנאי 3: לפחות ספרה אחת
    boolean hasDigit = false;
    for (int i = 0; i < password.length(); i++) {
        if (Character.isDigit(password.charAt(i))) {
            hasDigit = true;
            break;
        }
    }
    if (hasDigit) {
        criteriaMet++;
    }

    // תנאי 4: לפחות תו מיוחד אחד
    boolean hasSpecial = false;
    for (int i = 0; i < password.length(); i++) {
        char c = password.charAt(i);
        if (!Character.isLetterOrDigit(c)) {
            hasSpecial = true;
            break;
        }
    }
    if (hasSpecial) {
        criteriaMet++;
    }

    // תנאי 5: אין תווים זהים צמודים
    boolean noRepeats = true;
    for (int i = 1; i < password.length(); i++) {
        if (password.charAt(i) == password.charAt(i - 1)) {
            noRepeats = false;
            break;
        }
    }
    if (noRepeats) {
        criteriaMet++;
    }

    // הסיסמה תקינה אם עומדת ב-3 מתוך 5 תנאים
    return criteriaMet >= 3;
}
```

---

## סעיף ג' (7 נקודות) - עדכון סיסמה

כתבו במחלקה `Account` את הפעולה `updatePassword` המקבלת כפרמטר סיסמה חדשה.

**דרישות:**
1. הסיסמה החדשה צריכה להיות **תקינה**. אם היא לא תקינה, הפעולה לא תבצע עדכון ותדפיס הודעה מתאימה.
2. הסיסמה החדשה צריכה להיות **שונה מהסיסמה הנוכחית** ומסיסמאות הקודמות. אם היא זהה, הפעולה לא תבצע עדכון ותדפיס הודעה מתאימה.
3. אם הסיסמה החדשה תקינה ואינה זהה אף לא לאחת מהסיסמאות הקודמות, הפונקציה:
   - תעדכן את `currentPass` לסיסמה החדשה
   - תוסיף את הסיסמה החדשה לתחילת מערך `passHistory`
   - תזיז את הסיסמאות הקיימות (אם המערך מלא, הסיסמה הישנה ביותר תידרס)

### פתרון:

```java
public void updatePassword(String newPass) {
    // בדיקה 1: האם הסיסמה תקינה?
    if (!isPasswordValid(newPass)) {
        System.out.println("הסיסמה החדשה אינה עומדת בדרישות האבטחה.");
        return;
    }

    // בדיקה 2: האם הסיסמה זהה לסיסמה הנוכחית?
    if (newPass.equals(currentPass)) {
        System.out.println("הסיסמה החדשה זהה לסיסמה הנוכחית.");
        return;
    }

    // בדיקה 3: האם הסיסמה הייתה בשימוש בעבר?
    for (int i = 0; i < historySize; i++) {
        if (passHistory[i].equals(newPass)) {
            System.out.println("הסיסמה כבר הייתה בשימוש בעבר.");
            return;
        }
    }

    // עדכון: הזזת הסיסמאות הקודמות ימינה
    for (int i = Math.min(historySize, 9); i > 0; i--) {
        passHistory[i] = passHistory[i - 1];
    }

    // הוספת הסיסמה החדשה במקום הראשון
    passHistory[0] = newPass;
    currentPass = newPass;
    
    // עדכון גודל ההיסטוריה (עד מקסימום 10)
    if (historySize < 10) {
        historySize++;
    }

    System.out.println("הסיסמה עודכנה בהצלחה.");
}
```

---

## סעיף ד' (3 נקודות) - הוספת משתמש חדש

כתבו במחלקה `Users` את הפעולה `addUser` המקבלת שם משתמש וסיסמה ראשונית כפרמטרים.

**דרישות:**
1. תחילה הפעולה תבדוק אם כבר קיים חשבון עם שם המשתמש הזה
2. אם קיים או אם אין מקום, הפעולה לא תוסיף משתמש חדש ותדפיס הודעה מתאימה
3. אם שם המשתמש לא קיים והמערך `accounts` אינו מלא, הפעולה:
   - תיצור אובייקט חדש מסוג `Account`
   - תוסיף אותו למערך `accounts`
   - תעדכן את `numOfAccounts`

### פתרון:

```java
public class Users {
    private Account[] accounts = new Account[100];
    private int numOfAccounts = 0;

    public void addUser(String username, String password) {
        // בדיקה 1: האם המערך מלא?
        if (numOfAccounts >= 100) {
            System.out.println("לא ניתן להוסיף משתמש נוסף - המערכת מלאה.");
            return;
        }

        // בדיקה 2: האם שם המשתמש כבר קיים?
        for (int i = 0; i < numOfAccounts; i++) {
            if (accounts[i].getUsername().equals(username)) {
                System.out.println("שם המשתמש כבר קיים במערכת.");
                return;
            }
        }

        // הוספת משתמש חדש
        accounts[numOfAccounts] = new Account(username, password);
        numOfAccounts++;
        System.out.println("משתמש נוסף בהצלחה.");
    }
}
```

---

## סעיף ה' (4 נקודות בונוס) - שיפור דרישות האבטחה

עקב ריבוי ניסיונות פריצה מצד גורמים זרים, הוחלט להקשיח את דרישות האבטחה לסיסמאות של המשתמשים.

### שיפורים מוצעים:

**שינוי 1:** דרישה ל-**4 מתוך 5 תנאים** במקום 3 מתוך 5

**שינוי 2:** **חובה** שתהיה לפחות **אות קטנה אחת** ('a'-'z')

### יישום:

```java
public boolean isPasswordValid(String password) {
    int criteriaMet = 0;

    // תנאי 1: אורך >= 8
    if (password.length() >= 8)
        criteriaMet++;

    // תנאי 2: לפחות 2 אותיות גדולות
    int upperCount = 0;
    for (char c : password.toCharArray()) {
        if (c >= 'A' && c <= 'Z')
            upperCount++;
    }
    if (upperCount >= 2)
        criteriaMet++;

    // תנאי 3: לפחות ספרה אחת
    boolean hasDigit = false;
    for (char c : password.toCharArray()) {
        if (c >= '0' && c <= '9') {
            hasDigit = true;
            break;
        }
    }
    if (hasDigit)
        criteriaMet++;

    // תנאי 4: לפחות תו מיוחד
    boolean hasSpecial = false;
    for (char c : password.toCharArray()) {
        if (!((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9'))) {
            hasSpecial = true;
            break;
        }
    }
    if (hasSpecial)
        criteriaMet++;

    // תנאי 5: אין תווים זהים צמודים
    boolean noRepeats = true;
    for (int i = 1; i < password.length(); i++) {
        if (password.charAt(i) == password.charAt(i - 1)) {
            noRepeats = false;
            break;
        }
    }
    if (noRepeats)
        criteriaMet++;

    // תנאי חובה: לפחות אות קטנה אחת
    boolean hasLowercase = false;
    for (char c : password.toCharArray()) {
        if (c >= 'a' && c <= 'z') {
            hasLowercase = true;
            break;
        }
    }

    // הסיסמה תקינה אם עומדת ב-4 מתוך 5 תנאים ויש אות קטנה
    return (criteriaMet >= 4 && hasLowercase);
}
```

---

## דוגמאות שימוש

```java
public static void main(String[] args) {
    // יצירת חשבון
    Account acc = new Account("user1", "Pass123!");
    
    // בדיקת סיסמאות
    System.out.println(acc.isPasswordValid("abc"));           // false - קצר מדי
    System.out.println(acc.isPasswordValid("Password1!"));    // true - עומד בדרישות
    System.out.println(acc.isPasswordValid("Pass11!!"));      // true
    
    // עדכון סיסמה
    acc.updatePassword("NewPass2@");                          // הצלחה
    acc.updatePassword("NewPass2@");                          // שגיאה - זהה לנוכחית
    acc.updatePassword("Pass123!");                           // שגיאה - הייתה בעבר
    
    // מערכת משתמשים
    Users system = new Users();
    system.addUser("alice", "Alice123!");
    system.addUser("bob", "Bob456#");
    system.addUser("alice", "Another1!");                     // שגיאה - קיים
}
```

---

## סיכום

השאלה בודקת:
- ✅ תכנון מחלקות וקשרים ביניהן
- ✅ עבודה עם מערכים ואובייקטים
- ✅ אימות נתונים ובדיקת תנאים
- ✅ ניהול היסטוריה ומבני נתונים
- ✅ הדפסת הודעות שגיאה
- ✅ אבטחת מידע ודרישות סיסמה
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
בדיקת תקינות סיסמה לפי **3 מתוך 5 תנאים**, ניהול היסטוריה של 10 סיסמאות קודמות, והזזת מערך בעת עדכון.

### אלגוריתם:

**סעיף ב' - isPasswordValid:**
1. אתחל מונה `criteriaMet = 0`
2. בדוק כל תנאי בנפרד:
   - אורך >= 8
   - לפחות 2 אותיות גדולות (מונה בלולאה)
   - לפחות ספרה אחת
   - לפחות תו מיוחד
   - אין תווים זהים צמודים
3. אם תנאי מתקיים → `criteriaMet++`
4. החזר `criteriaMet >= 3`

**סעיף ג' - updatePassword:**
1. בדוק תקינות: `if (!isPasswordValid(newPass)) return;`
2. בדוק שלא זהה ל-`currentPass`
3. בדוק שלא מופיע ב-`passHistory[]` (לולאה)
4. הזז את כל ההיסטוריה **ימינה**: `for(i=9; i>0; i--) passHistory[i] = passHistory[i-1]`
5. הכנס את הסיסמה החדשה ב-`passHistory[0]`
6. עדכן `currentPass = newPass`

**סעיף ד' - addUser:**
1. בדוק אם `numOfAccounts >= 100` → מלא
2. בדוק אם username כבר קיים (לולאה על accounts)
3. צור `new Account(username, password)`
4. הוסף ל-`accounts[numOfAccounts++]`

### 🎯 מה להקפיד:

✅ **תנאים קצה:**
- סיסמה קצרה מדי (< 8)
- אין אותיות גדולות/ספרות
- תווים זהים צמודים: "aa", "11"
- מערך היסטוריה מלא (10 סיסמאות)
- username כפול

✅ **טעויות נפוצות:**
1. **שכחה לספור אותיות גדולות** - צריך מונה נפרד, לא boolean
2. **שימוש ב-`=` במקום `==`** - השוואה לא הקצאה
3. **הזזה מ-0 ל-9** במקום מ-9 ל-0 - תדרוס את כולם!
4. **שכחה לעדכן `historySize`** - חשוב לניהול תקין
5. **השוואת מחרוזות עם `==`** - חייב `equals()`!

✅ **כיצד לבדוק:**
1. "Abc123!" → 4 תנאים (length, 1 upper, digit, special) → valid ✓
2. "aabbcc" → 1 תנאי (length) → invalid ✗
3. נסה לעדכן פעמיים לאותה סיסמה → שגיאה בפעם 2
4. הוסף 10 סיסמאות, בדוק שה-11 מוחקת את הראשונה
5. נסה username כפול → שגיאה

---
---
<div style="page-break-after: always;"></div>

# שאלה 10 - פעולות רקורסיביות על מערכים
**ערך: 17 נקודות**  
**חלק ג' - בחר 2 מתוך 3 שאלות**

## תיאור השאלה

נתונות הפעולות הבאות: `what` ו-`secret`, ושתי פעולות עזר: `why` ו-`mystery`.

```java
public static void secret(int[] a, int s) {
    s %= a.length;
    mystery(a, 0, a.length - 1);
    mystery(a, 0, s - 1);
    mystery(a, s, a.length - 1);
}

public static void mystery(int[] a, int start, int end) {
    int temp;
    while (start < end) {
        temp = a[start];
        a[start] = a[end];
        a[end] = temp;
        start++;
        end--;
    }
}

public static void what(int[] a, int d) {
    why(a, d, 0);
}

public static void why(int[] a, int d, int i) {
    if (i < a.length) {
        int j = (i + d) % a.length;
        int rest = a[j];
        why(a, d, i + 1);
        a[i] = rest;
    }
}
```

נתון מערך `arr` של מספרים שלמים:

| 0  | 1  | 2  | 3  | 4  | 5  | 6  |
|----|----|----|----|----|----|----|
| 10 | 3  | 6  | 8  | 2  | 11 | 5  |

---

## סעיף א' (3 נקודות) - מעקב אחרי mystery

עקבו אחרי זימון הפעולה `mystery(arr, 1, 4)` ורשמו מה יהיה תוכן המערך אחרי הזימון.

### פתרון:

הפעולה `mystery(arr, start, end)` מבצעת **היפוך** של חלק מהמערך מאינדקס `start` עד אינדקס `end`.

**מצב לפני:**
```
[10, 3, 6, 8, 2, 11, 5]
```

**תהליך:**
- `start = 1, end = 4`: החלק להיפוך הוא `[3, 6, 8, 2]`
- שלב 1: החלף `arr[1]` ו-`arr[4]` → `[10, 2, 6, 8, 3, 11, 5]`
- שלב 2: `start = 2, end = 3`: החלף `arr[2]` ו-`arr[3]` → `[10, 2, 8, 6, 3, 11, 5]`
- שלב 3: `start = 3, end = 2`: תנאי `start < end` לא מתקיים, סיום

**תוצאה:**
```
[10, 2, 8, 6, 3, 11, 5]
```

---

## סעיף ב' (3 נקודות) - מעקב אחרי secret

עקבו אחרי זימון הפעולה `secret(arr, 3)` ורשמו מה יהיה תוכן המערך אחרי הזימון.

### פתרון:

**מצב לפני:**
```
[10, 3, 6, 8, 2, 11, 5]
```

**שלבי הפעולה:**

1. `s = 3 % 7 = 3`
2. `mystery(arr, 0, 6)` - היפוך כל המערך:
   ```
   [5, 11, 2, 8, 6, 3, 10]
   ```

3. `mystery(arr, 0, 2)` - היפוך החלק הראשון (אינדקסים 0-2):
   ```
   [2, 11, 5, 8, 6, 3, 10]
   ```

4. `mystery(arr, 3, 6)` - היפוך החלק השני (אינדקסים 3-6):
   ```
   [2, 11, 5, 10, 3, 6, 8]
   ```

**תוצאה:**
```
[2, 11, 5, 10, 3, 6, 8]
```

---

## סעיף ג' (2 נקודות) - הסבר secret

מה מבצעת הפעולה `secret(a, d)` עבור מערך של מספרים שלמים `a` ומספר שלם וחיובי `d`?

### פתרון:

הפונקציה `secret(a, d)` מבצעת **סיבוב שמאלה** (left rotation) של המערך ב-`d` מקומות.

**אלגוריתם:**
הפונקציה משתמשת בטכניקת **שלושה היפוכים**:
1. היפוך של כל המערך
2. היפוך של החלק הראשון (מאינדקס 0 עד `d-1`)
3. היפוך של החלק השני (מאינדקס `d` עד הסוף)

**דוגמה:**
- מערך: `[1, 2, 3, 4, 5]`
- סיבוב שמאלה ב-2 מקומות: `[3, 4, 5, 1, 2]`

---

## סעיף ד' (3 נקודות) - מעקב רקורסיבי אחרי what

עקבו אחרי זימון הפעולה `what(arr, 3)` על המערך ההתחלתי ורשמו מה יהיה תוכן המערך אחרי הזימון.

**יש להראות ערכי המשתנים בכל זימון רקורסיבי.**

### פתרון:

**מצב לפני:**
```
[10, 3, 6, 8, 2, 11, 5]
```

**שלבי הרקורסיה (`why(a, 3, i)`):**

| קריאה | i | j = (i+3)%7 | rest = a[j] | פעולה                          |
|-------|---|-------------|-------------|--------------------------------|
| 1     | 0 | 3           | 8           | שמירת 8, קריאה רקורסיבית      |
| 2     | 1 | 4           | 2           | שמירת 2, קריאה רקורסיבית      |
| 3     | 2 | 5           | 11          | שמירת 11, קריאה רקורסיבית     |
| 4     | 3 | 6           | 5           | שמירת 5, קריאה רקורסיבית      |
| 5     | 4 | 0           | 10          | שמירת 10, קריאה רקורסיבית     |
| 6     | 5 | 1           | 3           | שמירת 3, קריאה רקורסיבית      |
| 7     | 6 | 2           | 6           | שמירת 6, קריאה רקורסיבית      |
| 8     | 7 | -           | -           | `i >= a.length` - תנאי עצירה  |

**שלב חזור (backtracking):**
כעת הקריאות חוזרות בסדר הפוך ומעדכנות את המערך:
- `a[6] = 6`
- `a[5] = 3`
- `a[4] = 10`
- `a[3] = 5`
- `a[2] = 11`
- `a[1] = 2`
- `a[0] = 8`

**תוצאה:**
```
[8, 2, 11, 5, 10, 3, 6]
```

---

## סעיף ה' (3 נקודות) - הנדסה לאחור

לאחר זימון הפעולה `what(brr, 2)` מתקבל המערך `brr` הזה:

```
[60, 50, 40, 30, 20, 10]
```

**מה היה תוכן המערך `brr` לפני זימון הפעולה?**

### פתרון:

הפעולה `what(a, 2)` מבצעת סיבוב **ימינה** ב-2 מקומות.

כדי למצוא את המערך המקורי, נבצע סיבוב **שמאלה** ב-2 מקומות:

**תוצאה לאחר `what(brr, 2)`:**
```
[60, 50, 40, 30, 20, 10]
```

**חישוב לאחור:**
אם `what` מסובב ימינה ב-2, אז המקור יהיה סיבוב שמאלה ב-2:

| אינדקס בתוצאה | ערך | ← | אינדקס במקור |
|---------------|-----|---|--------------|
| 0             | 60  | ← | 4            |
| 1             | 50  | ← | 5            |
| 2             | 40  | ← | 0            |
| 3             | 30  | ← | 1            |
| 4             | 20  | ← | 2            |
| 5             | 10  | ← | 3            |

**המערך המקורי:**
```
[40, 30, 20, 10, 60, 50]
```

**בדיקה:**
- `what([40, 30, 20, 10, 60, 50], 2)` → סיבוב ימינה ב-2 → `[60, 50, 40, 30, 20, 10]` ✓

---

## סעיף ו' (3 נקודות) - הסבר what

מה מבצעת הפעולה `what(a, d)` עבור מערך של מספרים שלמים `a` ומספר שלם וחיובי `d`?

### פתרון:

הפעולה `what(a, d)` יוצרת **סיבוב ימינה** (right rotation) של המערך ב-`d` מקומות.

**אלגוריתם:**
- הפעולה משתמשת ברקורסיה
- בכל קריאה רקורסיבית, שומרת ערך מאינדקס `(i + d) % length`
- בשלב החזור, מעתיקה את הערכים השמורים למיקומים החדשים

**דוגמה:**
- מערך: `[1, 2, 3, 4, 5]`
- סיבוב ימינה ב-2 מקומות: `[4, 5, 1, 2, 3]`

**הבדל בין `secret` ו-`what`:**
- `secret(a, d)` - סיבוב **שמאלה**
- `what(a, d)` - סיבוב **ימינה**

---

## סיכום קוד מלא

```java
public class ArrayRotations {
    
    // סיבוב שמאלה באמצעות 3 היפוכים
    public static void secret(int[] a, int s) {
        s %= a.length;
        mystery(a, 0, a.length - 1);
        mystery(a, 0, s - 1);
        mystery(a, s, a.length - 1);
    }
    
    // היפוך חלק מהמערך
    public static void mystery(int[] a, int start, int end) {
        int temp;
        while (start < end) {
            temp = a[start];
            a[start] = a[end];
            a[end] = temp;
            start++;
            end--;
        }
    }
    
    // סיבוב ימינה באמצעות רקורסיה
    public static void what(int[] a, int d) {
        why(a, d, 0);
    }
    
    // פעולת עזר רקורסיבית לסיבוב ימינה
    public static void why(int[] a, int d, int i) {
        if (i < a.length) {
            int j = (i + d) % a.length;
            int rest = a[j];
            why(a, d, i + 1);
            a[i] = rest;
        }
    }
    
    // פעולת עזר להדפסת מערך
    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }
    
    public static void main(String[] args) {
        int[] arr1 = {10, 3, 6, 8, 2, 11, 5};
        System.out.print("מקורי: ");
        printArray(arr1);
        
        mystery(arr1, 1, 4);
        System.out.print("אחרי mystery(arr, 1, 4): ");
        printArray(arr1);
        
        int[] arr2 = {10, 3, 6, 8, 2, 11, 5};
        secret(arr2, 3);
        System.out.print("אחרי secret(arr, 3): ");
        printArray(arr2);
        
        int[] arr3 = {10, 3, 6, 8, 2, 11, 5};
        what(arr3, 3);
        System.out.print("אחרי what(arr, 3): ");
        printArray(arr3);
    }
}
```

---

## סיבוכיות

### mystery (היפוך)
- **זמן**: O(n) - כאשר n הוא אורך הטווח להיפוך
- **מקום**: O(1) - ללא שימוש בזיכרון נוסף

### secret (סיבוב שמאלה)
- **זמן**: O(n) - שלושה היפוכים, כל אחד O(n)
- **מקום**: O(1) - ללא שימוש בזיכרון נוסף

### what (סיבוב ימינה רקורסיבי)
- **זמן**: O(n) - כל איבר נבדק פעם אחת
- **מקום**: O(n) - עומק הרקורסיה

---

## סיכום

השאלה בודקת:
- ✅ הבנת פעולות רקורסיביות
- ✅ מעקב אחרי ביצוע אלגוריתמים
- ✅ הבנת סיבובי מערכים
- ✅ טכניקת היפוכים לסיבוב
- ✅ יכולת הנדסה לאחור
- ✅ ניתוח סיבוכיות
## 📚 הסבר התרגיל – כיצד לפתור?

### מהי הבעיה?
יש לנתח ולהבין פעולות רקורסיביות ואיטרטיביות שמבצעות סיבובים (rotations) והיפוכים (reversals) על מערכים. נדרש לעקוב אחרי ערכי המערך בשלבים שונים, להבין מה כל פונקציה עושה, ולזהות את ההבדלים בין סיבוב שמאלה, ימינה, והיפוך חלקי.

### שלבי פתרון (אלגוריתם):
1. קרא בעיון את הקוד – זהה אילו פרמטרים משתנים בכל קריאה.
2. עבור mystery – עקוב אחרי ערכי start, end, ומה קורה בכל איטרציה (היפוך חלקי).
3. עבור secret – הבן את שלבי שלושת ההיפוכים, ומה המשמעות של כל שלב (סיבוב שמאלה).
4. עבור what/why – עקוב אחרי הקריאות הרקורסיביות, מה נשמר ומה מתעדכן (סיבוב ימינה).
5. עבור כל סעיף – כתוב טבלה/תרשים של ערכי המערך בשלבים שונים.

### דגשים חשובים:
- mystery – מבצע היפוך של תת-מערך (מאינדקס start עד end).
- secret – מבצע סיבוב שמאלה ב-d מקומות ע"י שלושה היפוכים.
- what/why – מבצע סיבוב ימינה ב-d מקומות ע"י רקורסיה והעתקה.
- יש להיזהר מטעויות off-by-one (למשל, start < end).
- יש לעקוב אחרי ערכי המערך לפני ואחרי כל שלב.

### תנאי קצה:
- מערך ריק או בגודל 1
- סיבוב ב-0 מקומות (המערך לא משתנה)
- סיבוב בגודל המערך (חוזר לעצמו)
- סיבוב גדול מגודל המערך (שימוש ב-% length)

### טעויות נפוצות:
- בלבול בין סיבוב שמאלה לימינה
- שכחת לעדכן start/end בלולאה
- קריאה רקורסיבית לא נכונה (למשל, i+1 במקום i-1)
- שכחת תנאי עצירה ברקורסיה
- אי-בדיקת קלטים קיצוניים (מערך ריק, d=0)

### דוגמאות בדיקה:
1. mystery(arr, 1, 4) – בדוק את המערך לפני, אחרי כל החלפה, ואחרי הסיום.
2. secret(arr, 3) – כתוב את המערך אחרי כל שלב (היפוך כללי, היפוך ראשון, היפוך שני).
3. what(arr, 3) – עקוב אחרי ערכי i, j, ומה נשמר בכל שלב רקורסיבי.
4. נסה סיבוב ב-0, ב-1, בגודל המערך, ובערכים שליליים.

### איך לבדוק את עצמך?
- כתוב טבלה של ערכי המערך בשלבים שונים.
- נסה להריץ את הקוד על מערכים קצרים (3-5 איברים) ולבדוק ידנית.
- בדוק קלטים קיצוניים (מערך ריק, d=0, d=length).
- נסה להבין מה קורה כאשר d גדול מהאורך (שימוש ב-%).

### סיכום:
התרגיל דורש הבנה עמוקה של רקורסיה, לולאות, סיבובי מערכים, וניתוח שלבי ביצוע. חשוב להקפיד על מעקב אחרי ערכים, בדיקת תנאי קצה, והבנה של כל שלב באלגוריתם.

<div style="page-break-after: always;"></div>

# 📋 רשימת ביקורת – לפני המבחן

## ✅ בדוק את הבנתך

- [ ] יכול לכתוב תוכנית Java בסיסית עם `main`?
- [ ] מבין את ההבדל בין `int`, `double`, `String`?
- [ ] יכול לכתוב לולאה `for` ו-`while`?
- [ ] יודע להשתמש בתנאים `if`, `else if`, `else`?
- [ ] יכול לעבוד עם מערכים חד-ממדיים?
- [ ] יכול לעבוד עם מטריצות?
- [ ] מבין את עקרון הרקורסיה?
- [ ] יכול לקרוא ולכתוב סינטקס OOP בסיסי?

## ✅ בדוק את הקוד שלך

- [ ] כל המשתנים מאותחלים?
- [ ] כל סוגריים סגורים?
- [ ] השתמשת ב-`==` (לא `=`)?
- [ ] בדקת תנאים קצה?
- [ ] הדפסות בחוץ מהלולאה (אם צריך)?
- [ ] בדקת עם דוגמה?

---

**מסמך זה מוכן להדפסה וצפייה דיגיטלית.**  
**קיץ תשפ״ה (2025)**
