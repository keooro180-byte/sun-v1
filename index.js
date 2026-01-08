export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // مسار معالجة الطلبات الذكية
    if (url.pathname === "/chat") {
      const { message } = await request.json();
      const apiKey = env.GEMINI_API_KEY; // هنا سيقرأ السيرفر المفتاح الذي سنضعه
      
      // كود الربط المباشر مع Google Gemini API
      const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${apiKey}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contents: [{ parts: [{ text: message }] }] })
      });
      
      const data = await response.json();
      return new Response(JSON.stringify(data), { headers: { "Content-Type": "application/json" } });
    }

    // تشغيل الواجهة الرسومية (index.html)
    return await env.ASSETS.fetch(request);
  }
};
