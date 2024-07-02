import { StartupType } from "@/app/types";

export const fetchYCUrls = async (url: string) => {
    const response = await fetch(`/api/yc/fetchurls?url=${encodeURIComponent(url)}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}

export const checkIfUrlExists = async (scraped_url: string) => {
    const response = await fetch(`/api/startups/findexisting?scraped_url=${encodeURIComponent(scraped_url)}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const exists = await response.json();
    return exists;
}

export const scrapeSinglePage = async (url: string) => {
    const response = await fetch(`/api/yc/scrapecompanypage?url=${encodeURIComponent(url)}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}

export const saveStartup = async (startup: StartupType) => {
    try {
        const response = await fetch("/api/startups", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(startup)
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
    } catch (error) {
        console.error("Failed to save URLs:", error);
    }
};