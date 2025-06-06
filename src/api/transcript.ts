// src/api/transcript.ts

// Extracts video ID from YouTube URL
export function extractVideoId(url: string): string | null {
  const regex = /(?:v=|youtu\.be\/|\/embed\/|\/v\/)([A-Za-z0-9_\-]{11})/;
  const match = url.match(regex);
  return match ? match[1] : null;
}

// Fetch transcript from Python API
export async function fetchTranscript(videoId: string) {
  const res = await fetch(`http://localhost:5000/api/transcript?videoId=${videoId}`);
  if (!res.ok) throw new Error('Transcript API did not return JSON');
  return await res.json();
}
