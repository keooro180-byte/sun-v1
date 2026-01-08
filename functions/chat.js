const fetch = require('node-fetch');

exports.handler = async (event) => {
    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "POST, OPTIONS"
    };

    if (event.httpMethod === "OPTIONS") return { statusCode: 200, headers };

    try {
        const { message } = JSON.parse(event.body);
        const apiKey = process.env.GEMINI_API_KEY;

        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                contents: [{ parts: [{ text: message }] }]
            })
        });

        const data = await response.json();
        const reply = data.candidates[0].content.parts[0].text;

        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({ reply })
        };
    } catch (error) {
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: "فشل في تشغيل المحرك الذكي" })
        };
    }
};
