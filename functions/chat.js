hereexports.handler = async (event) => {
  const { message } = JSON.parse(event.body);
  const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${process.env.GEMINI_API_KEY}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ contents: [{ parts: [{ text: message }] }] })
  });
  const data = await response.json();
  return { statusCode: 200, body: JSON.stringify(data) };
};
