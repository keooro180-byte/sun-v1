export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // مسار معالجة الطلبات الذكية
    if (url.pathname === "/chat" && request.method === "POST") {
      try {
        const { message } = await request.json();
        const apiKey = env.GEMINI_API_KEY; 
        
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ contents: [{ parts: [{ text: message }] }] })
        });
        
        const data = await response.json();
        return new Response(JSON.stringify(data), { 
          headers: { "Content-Type": "application/json" } 
        });
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 });
      }
    }

    // إذا لم يكن الطلب لـ /chat، حاول تقديم الملفات الثابتة
    return env.ASSETS.fetch(request);
  }
};
