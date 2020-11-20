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
* Standard

##### Name
وەکو ستانداردی پرۆژەکە سێ پۆست لەسەرەتا هەن:

* Super Admininstrator
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
        <th>Standard</th>
    </tr>
    <tr>
        <td>NewManager</td>
        <td>New Manager</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Manager</td>
        <td>Manager</td>
        <td>1</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DeactivatingManager</td>
        <td>Inactive Manager</td>
        <td>1</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DisabledManager</td>
        <td>Disabled Manager</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>ActivatingManager</td>
        <td>Disabled Manager</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>UpgradingManager</td>
        <td>Manager</td>
        <td>1</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Administrator</td>
        <td>Administrator</td>
        <td>10</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DeactivatingAdministrator</td>
        <td>Inactive Administrator</td>
        <td>10</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DisabledAdministrator</td>
        <td>Disabled Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>ActivatingAdministrator</td>
        <td>Disabled Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DowngradingAdministrator</td>
        <td>Inactive Administrator</td>
        <td>10</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>UpgradingAdministrator</td>
        <td>Administrator</td>
        <td>10</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>SuperAdministrator</td>
        <td>Super Administrator</td>
        <td>25</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DeactivatingSuperAdministrator</td>
        <td>Inactive Super Administrator</td>
        <td>25</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DisabledSuperAdministrator</td>
        <td>Disabled Super Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>ActivatingSuperAdministrator</td>
        <td>Disabled Super Administrator</td>
        <td>0</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>DowngradingSuperAdministrator</td>
        <td>Inactive Super Administrator</td>
        <td>25</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>UpgradingAdministrator</td>
        <td>Administrator</td>
        <td>10</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
</table>


 
## Staff Entity:
بۆ زانیاری ستافی پشتەوە
فێڵدەکان:
* *Id*
* *Backend Rolde Id*
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

#### Backend Role Id

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


