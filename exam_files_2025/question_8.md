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