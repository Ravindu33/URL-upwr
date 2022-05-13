class Translation(object):
    START_TEXT = """😁කොහොමද{},
මම RX-Uploader!🤖
💁ඔයාට පුළුවන් HTTP/HTTPS🧐 වලින් තියෙන direct links 😏 මගෙන්🤖 කෙලින්ම අප්ලෝඩ් කරගන්න💯🤘!

/help for more details!"""
    FORMAT_SELECTION = "ඔබට අවශ්‍ය ෆයිල් ෆෝමැට් එක තෝරන්න: <a href='{}'>ෆයිල් එකේ ප්‍රමාණය අඩුනම් හොඳයි</a> \nඔබට thumbnail වෙනස් කළ යුතු button වලින් එකක් ඔබපු වහාම මට අවශ්‍ය පින්තූරය ඒවන්න.\n /deletethumbnail 👈මෙයින් ඉබේ දමන thumbnail එක delete කළ හැක."
    SET_CUSTOM_USERNAME_PASSWORD = """ඔබට pasword🚧වලින් සුරක්ෂිත🔒කරන ලද වීඩියෝස්🎥ඩවුන්ලෝඩ්⬇️කළ යුතු නම් පහත👇ලෙස තොරතුරු තනි msg📤එකකින් ඒවන්න..
ලින්කුව | නව නම | username | password"""
    DOWNLOAD_START = "📥Downloading...🗄️"
    UPLOAD_START = "📤Uploading...🚀"
    RCHD_TG_API_LIMIT = "🛬Downloaded in {} seconds.\n🧐Detected File Size: {}\n🤕සමාවෙන්න මට තවම 2GB🗄️ ට වඩා වැඩි ෆයිල්📂 අප්ලෝඩ් කරද්දී පොඩි ප්‍රශ්න😤 කිහිපයක් තියේ 😏.මගේ මාස්ටර් ඒව හරිගස්සනකම් ඉන්න වෙනවා😌"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "😌මාව භාවිතා🚀 කලාට ස්තුතියි🙏.\n\n<b>📤updates හා වැඩි📝විස්තර සඳහා අපගේ චැනල්📢එකට එකතු වෙන්න👉 : @RXbots</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@RX_Uploader_bot"
    SAVED_CUSTOM_THUMB_NAIL = "🖼️thumbnail එක සැකසුවා⚙️.🎥ඊළග වීඩියෝ වලට මෙය මම🤖යොදනවා💁."
    DEL_ETED_CUSTOM_THUMB_NAIL = "🧐සැකසූ thumbnali🖼️ එක අයින් කරා😏මීළග වීඩියෝවට🎥ඉබේ සැකසූ tumbnail🖼️එකක් මම🤖යොදනවා😌🙏"
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "🛑ගැටලුවක්🛑...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """🤖මාව භාවිතා💁 කරන්නේ කෙසේද🧐? පහත පියවර😌 අනුගමනය කරන්න👇!
    
1. 🚀link එක ඒවන්න💁[ 🛑direct link එකක් විය යුතුයි🛑 ](උදා: ලින්කුව | නව නමක් එක්කළ යුතු නම් එම නම.mp4).
{🛑<pre>|</pre>👈නව නමක් එක්කරන්නේ නම් මෙම ලකුණ අත්‍යවශ්‍ය වේ.🛑 }

2. Thumbnail🖼️එක වෙනස්⚙️කළ යුතුනම් අවශ්‍ය පින්තූරය🖼️ඒවන්න.සෙට්ටිංවලින්⚙️වෙනස් කළ හැක😌.(Optional).

3. ඔබට ෆයිල්📁ඕන විදිහ💁තෝරන්න👇.
   SVideo - 🎥වීඩියෝ එකක් ස්ක්‍රීන්ෂෝට්🖼️ සමග(ටෙලිග්‍රෑම්🚀තුළ ප්ලේ▶️කළ හැක).
   DFile  - ෆයිල් එකක් ස්ක්‍රීන්ෂෝට්🖼️ සමග(ටෙලිග්‍රෑම්🚀තුළ ප්ලේ▶️කළ නොහැක,ඩවුන්ලෝඩ් කළ පසු හැක).
   Video  - වීඩියෝව🎥 පමණක්☝️
   File   - ෆයිල්📁 එක පමණක්☝️

🤖බොට් වැඩ නැත්තං🛑මගේ🤖owners ල contact📞කර ගන්න.😌 @RX_bots"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "/generatecustomthumbnail 👈මෙය reply🚀කිරීමෙන් ඉබේ යොදන thumbnail 🖼️ එකක් සකස්💁කාල හැක.🤗"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
ඔබට මෙය භාවිතා කළ හැක්කේ👉/rename 📁ෆයිල් ලැබුණු පසු,එහි නම📝වෙනස් කිරීමට හා thumbnail🖼️එක වෙනස් කිරීමටයි😌.
"""
    CANCEL_STR = "Process⚙️Cancelled🤫"
    ZIP_UPLOADED_STR = "📤Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "හපෝ🤯,ඔයා දුන්නු url🌝එක පට්ට slow🤮නේ.මට ඒක ඩවුන්ලෝඩ්⬇️කරන්න කම්මැලි😴,අනික එකෙන් මාව භාවිතා😌කරන අනිත් අයගේ process⚙️පවා slow🤮වෙනවා.ඔන්නම් ඔයා මේ url🚀එකට ගිහින්👇මට fast🚀url එක ගැනත් දෙන්න මම ඒක upload📤කරන්නම්🤗:==> https://shrtz.me/PtsVnf6 "
