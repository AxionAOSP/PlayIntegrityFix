# 🧩 Axion OS – Play Integrity Fix Guide

This guide will help you fix **Google Play Integrity** and pass all available integrity levels:

- ✅ **Basic Integrity**
- ✅ **Device Integrity**
- ✅ **Strong Integrity**

Follow the steps carefully 👇

---

## ⚙️ Passing Basic Integrity

1. Open **Settings**
2. Navigate to **Axion Hub → Essentials → Play Integrity Fix**
3. Tap **Fetch Pixel Beta**

🎉 **Done!**  
After completing these steps, your device should now **pass Basic Integrity**.

---

## 🔐 Passing Strong Integrity

To pass **Strong Integrity**, a **valid keybox** is required.

### 📌 Steps

1. Obtain a **valid keybox XML** from a trusted source  
   > ⚠️ Keyboxes are **not provided**. You must find one yourself.
2. Open **Axion Hub → Essentials → Tricky Store**
3. Tap **Import Keybox** and load your valid keybox file
4. Open **Manage Target Apps**
   - Search for **Google Play Services** and **Google Play Store**
   - Select:
     - **Leaf? 🍃** → If your device has a **working TEE**
     - **Gen! ⚙️** → If your device has a **broken TEE**  
       *(Common on OnePlus, Moto, etc.)*
5. Recheck your **Play Integrity** status

🎉 You should now **pass Strong Integrity**!

> ⚠️ **Important:**  
> Always **delete the existing keybox** before importing a new one  
> (**Tricky Store → Delete Keybox**)

---

## ⚙️ Passing up to Device Integrity (Basic + Device)

- Previously, spoofing the **Play Store** allowed passing **Device Integrity**, but Google has now **patched** this method.
- If Google **soft-bans keyboxes**, a keybox that previously passed **Strong Integrity** may still allow passing **up to Device Integrity**.

---

## 📝 Notes & Warnings

- 🔄 Google may change Play Integrity behavior **at any time** — enjoy it while it lasts.
- ❌ Do **not abuse keyboxes** just for flexing. Use them **only when necessary**.
- 📱 **Android 15 builds** → [Follow the keybox conversion guide](https://github.com/AxionAOSP/PlayIntegrityFix/blob/lineage-22.1/keybox/Keybox_conversion.md)
- 🧱 **Axion builds v2.0 – v2.2.1** → [Follow this guide](https://github.com/AxionAOSP/PlayIntegrityFix/blob/lineage-22.1/keybox/old.md)

---

💡 **Tip:**  
Keep your setup minimal and responsible — this helps Play Integrity remain functional longer on **Axion OS**.
