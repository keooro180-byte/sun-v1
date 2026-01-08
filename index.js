/**
 * SUN OS V1.0 - Core Engine (2026)
 * نظام الإدارة السيادية الدائمة
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // 1. مسار معالجة المحادثة (/chat)
    if (url.pathname === "/chat" && request.method === "POST") {
      try {
        const { message } = await request.json();
        
        // جلب مفتاح API من المتغيرات البيئية
        const apiKey = env.GEMINI_API_KEY;
        if (!apiKey) {
          return new Response(JSON.stringify({ 
            candidates: [{ content: { parts: [{ text: "خطأ: مفتاح API غير موجود في إعدادات السيرفر." }] } }] 
          }), { status: 500 });
        }

        // الاتصال بنواة Gemini (إصدار 2026 المستقر)
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: [{ parts: [{ text: message }] }]
          })
        });

        const data = await response.json();
        return new Response(JSON.stringify(data), {
          headers: { "Content-Type": "application/json" }
        });

      } catch (error) {
        return new Response(JSON.stringify({ error: "فشل في معالجة الطلب" }), { status: 500 });
      }
    }

    // 2. تقديم الملفات الثابتة (واجهة المستخدم من مجلد public)
    return env.ASSETS.fetch(request);
  }
};

// Force Rebuild 2026.01.08
