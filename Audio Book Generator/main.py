# 🔊🎧 PYNEXUS - Your Personal PDF-to-Audio Converter 🚀
# Cool, Funky & Professional 🤘 by GuardiansOfCode
    
from gtts import gTTS
import PyPDF2
import os

# 📂 Load your PDF file
pdf_path = 'name.pdf'  # Replace with your PDF file
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

        total_pages = reader.numPages
        print(f"📖 Total pages found: {total_pages}")

        all_text = []

        # 🌀 Loop through all pages and extract text
        for page_num in range(total_pages):
            try:
                page = reader.getPage(page_num)
                text = page.extractText()
                if text.strip():
                    all_text.append(text)
                    print(f"✅ Page {page_num + 1} processed.")
                else:
                    print(f"⚠️ Page {page_num + 1} is empty or non-extractable.")
            except Exception as e:
                print(f"❌ Error on page {page_num + 1}: {e}")

        final_text = " ".join(all_text)

        # 💬 Language for the audio output
        language = 'en'

        # 🎶 Convert text to audio using gTTS
        print("🎤 Generating your funky audiobook... hang tight!")
        audio = gTTS(text=final_text, lang=language, slow=False)
        audio.save("PYNEXUS_Audio.mp3")

        print("✅ Done! Your audio file is saved as: PYNEXUS_Audio.mp3 🎧")

except FileNotFoundError:
    print(f"❌ PDF file '{pdf_path}' not found. Please check the path.")
except Exception as e:
    print(f"💥 Unexpected error: {e}")
