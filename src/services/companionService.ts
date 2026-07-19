export const COMPANION_URL = 'http://localhost:8080/api/command';

export async function sendCompanionCommand(action: string, payload?: any): Promise<boolean> {
  try {
    const response = await fetch(COMPANION_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ action, payload })
    });
    return response.ok;
  } catch (error) {
    console.error("Companion server not reachable:", error);
    return false;
  }
}
