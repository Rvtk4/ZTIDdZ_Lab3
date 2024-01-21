const base64Encode = (text) => {
  const encodedText = Buffer.from(text).toString('base64');
  return encodedText;
};

const base64Decode = (encodedText) => {
  const decodedText = Buffer.from(encodedText, 'base64').toString('utf-8');
  return decodedText;
};

// Przykład użycia:
const originalText = "Hello, World!";
const encodedText = base64Encode(originalText);

console.log("Zaszyfrowany tekst:", encodedText);

const decodedText = base64Decode(encodedText);
console.log("Odszyfrowany tekst:", decodedText);
