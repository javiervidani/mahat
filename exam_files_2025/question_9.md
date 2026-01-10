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