# Database:
پێکهاتووە لە چەندین بەش:

# Backend Part:
بەشی پشتەوە ئەو بەشەیە کە ستافی ئەدمینی وێبسایتەکەی تێدایە. بەگشتی بیرۆکەی ستافی پشتەوە ستافێکی دیموکراتییە. واتە هەر ئەندامێکی نوێ بێتە ناو ستافەکەوە و پلەبەرزبوونەوەی لەڕێگەی دەنگدانی ستافەکەوە دەبێت. نەک لەژێر فەرمانی کۆمەڵێکی بچووکی ستاف بێت. وردەکاری ئەمە لە دواتر زیاتر ڕوون دەبێتەوە.

خشتە (مۆدێل)ەکان بەگشتی ئەمانەن:
## Backend Role Entity:
ئەم خشتەیە داتای پلەبەندی ستافی پشتەوە تێدایە.

فێڵدەکان:
* *Id*
* Name
* Power
* Active
* Vote Time
* New
* Standard

##### Name
وەکو ستانداردی پرۆژەکە سێ پۆست لەسەرەتا هەن:

* Super Administrator
* Administrator
* Manager

هەروەها جگە لەمانە دواتر دەتوانرێت لەلایەن سوپەر ئەدمینەکانەوە پۆستی  تر زیاد بکرێت.

##### Power
هێزی پۆست دیاری دەکات، واتە هەندێک بڕیاری ستاف کە پێویست بە خستنە دەنگدان ئەکات. بەپێی هێزەکانیان دەنگدان دەکرێت، بە ستانداردی بەم شێوەیە:

<table>
  <tr>
    <th>Name</th>
    <th>Power</th>
  </tr>
  <tr>
    <td>Super Admin</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Admin</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Manager</td>
    <td>1</td>
  </tr>
</table>

مانای ئەمە چییە؟

کاتێک هەر گۆڕانکارییەک لە هەر شتێکدا دەکرێت لە بەشی پشتەوە، ئەو گۆڕانکارییە جێبەجێ ناکرێت تاوەکو بەگشتی ئەوانەی مافی دەنگدانیان ئەیگرێتەوە تا دەنگ بدەن لەسەر ئەو گۆڕانکارییە، بەگشتی ئەنجامی دەنگدان دەبێت لە ٪75 کەمتر نەبێت. 
هۆکاری ئەمەی هەر گۆڕانکارییەک دەنگدانی دەوێت ئەوەیە کە قۆرخکاری نەبێت لە کاری پشتەوەی ماڵپەڕەکە، دەبێت هەر گۆڕانکارییەک هەموو ئەدمین و سوپەر ئەدمینەکان قبوڵی بکەن یاخود ئەگەر بەڕێوەبەرەکانیش مافیان بەرکەوت ئەوانیش دەنگبدەن و قبوڵی بکەن، بەپێی گۆڕانکاریی و مافی دەنگدان.

نمونە:
زیادکردنی ستافێک یان گۆڕینی یاسایەکی تایبەت بە پشتەوەی ماڵپەڕە یاخود پێشەوەی ماڵپەڕەکە. یاخود وەستاندی بەڕێوەبەرێک.

بۆ نمونە وەستاندنی بەڕێوەبەرێک، دەچێتە دەنگدانەوە لە نێوان سوپەر ئەدمین و ئەدمین (کە مافی ئەمانە)، ئەو ڕێژەی هێزەکە دەبێتە پشکی هەر یەکێک لەوان. 

گریمان 3 سوپەر ئەدمین و 5 ئەدمین هەیە، یەکێک وەک بەڕێوەبەر تۆمار ئەکرێت، ئەو کاتە دەکەوێتە دەنگدان (تۆمارکەریش کە یەکێک دەبێت لە ئەدمین یاخود سوپەر ئەدمین، خۆی مافی دەنگدانی دەبێت، هەروەها کاتێک شتێک ئەکات واتە دەنگدان دروست ئەکات ، خۆی ئۆتۆماتیکی دەنگی حساب ئەکرێت ، واتە ئەوەی دەنگدان دروست ئەکات) :

<table>
  <tr>
    <th>Number</th>
    <th>Name</th>
    <th>Power</th>
    <th>Result</th>
  </tr>
  <tr>
    <td>2</td>
    <td>Super Admin</td>
    <td>25</td>
    <td>50</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Admin</td>
    <td>10</td>
    <td>50</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>100%</td>
  </tr>
</table>

بە گشتی کردییە 100 پشک ، دەبێت بەلایەنی کەمەوە 2 سوپەر ئەدمین و 3 ئەدمین دەنگی پێ بدەن. یان 1 سوپەر و 5 ئەدمین. کە ڕێژەی یاسایی تەواو بکات.

بەگشتی ئەوانەی لەکارخراون هێزیان دەبێت بە سفر ، واتە نە مافی دەنگدانیان ئەمێنێت، ناتوانێت بچێتە ناو ژمێرەکەی واتە مافی چوونەناوەوەی نامێنێت بۆ ناو بەشی ئەدمین.
 

##### Active
بۆ دیاری کردنی ئەوەی کە ئایا ئەو پۆستە مافی کارەکانی هەیە یاخود نا، مانای سڕکردن لە کارەکانی ، 
بەپێی خشتەی گشتی ئەوانەی پلەیان نزم ئەکرێتەوە یاخود بەرەو لەکارخستن دەبرێن، ناچالاک ئەکرێن. تەنها دەتوانن بچنە ناو دیوی پشتەوە و بتوانن دەنگ بدەن و ئاگایان لە چالاکی و کارەکان ببێت. هۆی ئەمە دەگەڕێتەوە بۆ ئەوەی ئەو کەسەی سڕ دەکرێت بەهۆکاری ڕق یان تۆڵە کاری تێکدەر نەکات. تاوەکو بەتەووی مافی بۆ دیاری دەکرێت.
ماوەی دەنگدان و وەرگرتنی ئەنجام نابێت لە مانگێک زیاتری پێ بچێت. ئەگەر لەو ماوەیەدا دەنگی تەواو کۆنەکرایەوە بۆ بڕیارەکە ئەوا ئەو دەنگدانە ئەچێتەوە سەر باری ئاسایی خۆی. ئەگەر کەسێک سڕکرا و دەنگی تەواوی بەدەست هێنا ئەوا ئەو کاتە هاتنە ناوەوەی نامێنێت. تەنها داتاکانی لە سیستەم دەمێنێت.
هەر کاتێک دەنگدان هەبوو ، ئەوانەی مافی دەنگدانیان هەبێت. لەگەڵ هەر داخڵبوونێکدا یەکسەر دەنگدانەکە بێتە بەردەمی و دەنگ بدات، تاوەکو دەنگ نەدات نەتوانێت بچێتە سەر بەشەکانی تر، بەڵام تا دووجار بۆی هەیە دوای بخات. لە سێیەم جاردا ئەبێت دەنگ بدات. ماوەی هەر داواکاری دەنگدانێک نابێت لە ڕۆژێک کەمتر بێت. واتە دوای یەک ڕۆژ تێپەڕی بێتەوە بەردەمی.

##### Vote Time
ئەو پۆستانەی کە پۆستی سەرەکین ئەمە بۆیان کۆژاوەتەوە، واتە وەکو ئەدمین و سوپەر ئەدمین و بەڕێوەبەر، ئەو پۆستانەی کە ئەچێتە ناو دەنگدانەوە ، واتە کاتێک دەنگدان لەسەر پلەبەرزکردنەوە یان داگرتن، یاخود وەستاندنی کەسێک دەکرێت یەکسەر دەچێتە سەر ئەم پۆستە و چاوەڕێی یەکلاییبوونەوەی دەنگدان دەکات تا بچێتە سەر پۆستی سەرەکی دواتری کە دیاریکراوە
##### New
ئەمە تەنها بۆ یەک پۆست داگیرساوبێت، بۆ ئەوانەی تر کوژاوە بێت. ئەمە ئەوە دیاری دەکات کاتێک ستافێکی نوێ زیاد دەکرێت چ پۆستێک وەردەگرێت. کە ئاسایی خۆی بەڕێوەەری نوێیە. 

##### Standard
ئەمە تەنها بۆ ئەم پۆستە ستانداردانە هەیە، کە سیستەمەکە دیاری دەکات. کاتێک پۆستی نوێ تۆمار بکرێت. ئەمەی بۆ چالاک ناکرێت. ئەمەش بۆ ئەوەیە ئەم تۆمارانە بەدوور بگیرێت لە لابردن لە سیستەمە.

ستافەکە بۆیان هەیە دەستکاری ڕێژەی هێزی پۆستە ستانداردەکان بکەن. (بێگومان دوای بەدەستهێنانی دەنگدان لەسەری) هەروەها دەتوانن پۆستی نوێش تۆمار بکەن. بەڵام نابێت هیچ پۆستێک هێزەکانیان وەکو یەک بێت.

خشتەی پۆستەکانی ستاف:
<table>
    <tr>
        <th>Id</th>
        <th>Name</th>
        <th>Power</th>
        <th>Active</th>
        <th>Vote Time</th>
        <th>New</th>
        <th>Standard</th>
    </tr>
    <tr>
        <td>New</td>
        <td>New</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Manager</td>
        <td>Manager</td>
        <td>1</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DeactivatingManager</td>
        <td>Inactive Manager</td>
        <td>1</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DisabledManager</td>
        <td>Disabled Manager</td>
        <td>0</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>ActivatingManager</td>
        <td>Disabled Manager</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>UpgradingManager</td>
        <td>Manager</td>
        <td>1</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Administrator</td>
        <td>Administrator</td>
        <td>10</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DeactivatingAdministrator</td>
        <td>Inactive Administrator</td>
        <td>10</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DisabledAdministrator</td>
        <td>Disabled Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>ActivatingAdministrator</td>
        <td>Disabled Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DowngradingAdministrator</td>
        <td>Inactive Administrator</td>
        <td>10</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>UpgradingAdministrator</td>
        <td>Administrator</td>
        <td>10</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>SuperAdministrator</td>
        <td>Super Administrator</td>
        <td>25</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DeactivatingSuperAdministrator</td>
        <td>Inactive Super Administrator</td>
        <td>25</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DisabledSuperAdministrator</td>
        <td>Disabled Super Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>ActivatingSuperAdministrator</td>
        <td>Disabled Super Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DowngradingSuperAdministrator</td>
        <td>Inactive Super Administrator</td>
        <td>25</td>
        <td>No</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
</table>

## Role Grading Entity:
لەم خشتەیەدا بەگشتی ئەو پۆستانەی کە فێڵدی کاتی دەنگدان واتە Vote Time یان داگیرساوە دێنە ئەم خشتەیە بۆ دیاریکردنی ئەوەی دوای یەکلایی بوونەوەی دەنگدان بچێتە سەر چ پۆستێک. 
* *Id*
* *Current Role Id* Current
* *Yes Role Id* Yes Vote
* *No Role Id* No Vote
* Standard

##### Current
پۆستێک کە لەدەنگداندایە
##### Yes Vote
پۆستێک دوای بەدەستهێنانی بەڵێ
##### No Vote
پۆستێک دوای بەدەستهێنانی نەخێر
##### Standard
بۆ ڕیکۆردە ستانداردەکان، واتە ئەمانەی ئەمەی بۆ دادەگیرسێت و ناتوانرێت لاببرێت بەڵام دەتوانرێت دەستکاری بکرێت. هەمان کاری هەیە وەکو خشتەی Backend Role

خشتەی پلەبەندی ستاف (ستاندار):


<table>
    <tr>
        <th>Current</th>
        <th>Yes Vote</th>
        <th>No Vote</th>
    </tr>
    <tr>
        <td>NewManger</td>
        <td>Manager</td>
        <td>DisabledManager</td>
    </tr>
    <tr>
        <td>DeactivatingManager</td>
        <td>DisabledManager</td>
        <td>Manager</td>
    </tr>
    <tr>
        <td>ActivatingManager</td>
        <td>Manager</td>
        <td>DisabledManager</td>
    </tr>
    <tr>
        <td>UpgradingManager</td>
        <td>Administrator</td>
        <td>Manager</td>
    </tr>
    <tr>
        <td>DeactivatingAdministrator</td>
        <td>DisabledAdministrator</td>
        <td>Administrator</td>
    </tr>
    <tr>
        <td>ActivatingAdministrator</td>
        <td>Administrator</td>
        <td>DisabledAdministrator</td>
    </tr>
    <tr>
        <td>DowngradingAdministrator</td>
        <td>Manager</td>
        <td>Administrator</td>
    </tr>
    <tr>
        <td>UpgradingAdministrator</td>
        <td>SuperAdministrator</td>
        <td>Administrator</td>
    </tr>
    <tr>
        <td>DeactivatingSuperAdministrator</td>
        <td>DisabledSuperAdministrator</td>
        <td>SuperAdministrator</td>
    </tr>
    <tr>
        <td>ActivatingSuperAdministrator</td>
        <td>SuperAdministrator</td>
        <td>DisabledSuperAdministrator</td>
    </tr>
    <tr>
        <td>DowngradingSuperAdministrator</td>
        <td>Administrator</td>
        <td>SuperAdministrator</td>
    </tr>
 </table>

 تێبینی:
 ئەم تێبینییە بۆ کاتی پڕۆگرامینە،
 کاتێک پلە ئەگۆڕدرێت بێگومان لە لیستی بەردەم بەکارهێنەر تەنها ئەو پۆستانە پیشاندەدرێت کە فێڵدی Vote Time کوژاوە بێت. ئینجا و ئەو پۆستەی تیا نابێت کە خۆی ئێستا ئەو پۆستەیە واتە کە بەڕێوەبەر بوو تەنها پۆستی دواتری پیشان دەدرێت، چۆن ئەو پۆستە ئەدۆزرێتەوە. لە ڕێگەی پاوەرەکەی کە بزانرێت سەروو خۆی کە پاوەرەکەی زیاتر بێت، خواروو خۆی کە پاوەرەکەی کەمتر بێت بەڵام سفر نەبێت. ئینجا ئەگەر ئیختیاری دەنگدان هەبێت لەناو سیستەمەکە لەم خشتەیە بگەڕێت لە فێڵدی نەخێر یەکسان بێت بەم پۆستەی ئێستای ، فێڵدی بەڵێ یەکسان بێت بۆ پۆستە نوێیەکە بەمە پلەکەی دەنگدانەکە دەدۆزرێتەوە، لەبەر ئەوەی بەڕێوەبەر بۆ بەڕێوەبەری وەستاو دوو ڕیکۆرد هەیە، بۆیە ئەم مەرجەش بەهەند وەرگیرێت کە فێڵدی نوێ New یش دەبێت کوژاوە بێت.
 هەر پلەیەکی نوێ زیاد دەکرێت پاوەری یان دەبێت سفر بێت یاخود لەنێوان دوو لە پۆستەکانی تردا بێت واتە سفر یان یەکسان نەبێت بە هیچ لەوانەی تر کە سفر نین. 

 هەر پۆستێک زیاد دەکرێت دەبێت دوو پۆست بەیەکەوە زیاد بکرێت بە شێوەیەک یەکیان بۆ چالاک و دووەمیان بۆ وەستێنراو هەروەها ئینجا بەلایەنی کەمەوە یەکێک لە پۆستەکان بۆ داگرتنی پلە دیاری بکرێت ، یاخود یەکێک بۆ بەرزکردنەوەی پلە دیاری بکرێت، یاخود هەردووکیان ، واتە بۆ هەر پۆستێکی نوێ سێ پۆستی بۆ دروست ئەکرێت بەلایەنی کەمەوە. چونکە پۆستی ئەمسەر و ئەوسەر وەکو بەڕێوەبەر و سوپەر ئەدمین پێویستیان بە هەردوو جۆرەکەی داگرتن و بەرزکردنەوە نییە. بەڵام بەپێی پاوەرکەی سەیر بکرێت ئەگەر نەکەوێتە ئەمسەر یان ئەوسەر ئەوا هەردووکی داوا بکات، ئەگەر کەوتە ئەمسەر و ئەوسەر ،ئەوا ئەو پلە نوخسانەی پلەکەی تریش داوابکات


## Staff Entity:
بۆ زانیاری ستافی پشتەوە
فێڵدەکان:
* *Id*
* *Backend Role Id*
* Username
* Email
* Password
* First Name
* Middle Name
* Last Name
* Birthdate
* Profile
* Mobile Number
* Photo
* Last Login
* Timestamp

##### Backend Role Id

##### Username
##### Email
##### Password
##### First Name
##### Middle Name
##### Last Name
##### Birthdate
##### Profile
##### Mobile Number
##### Photo
##### Last Login
##### Timestamp


