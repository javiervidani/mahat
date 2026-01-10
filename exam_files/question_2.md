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