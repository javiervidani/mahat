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