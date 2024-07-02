export const fetchEmbeddings = async (query: string) => {
    const response = await fetch(`/api/startups?query=${encodeURIComponent(query)}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}