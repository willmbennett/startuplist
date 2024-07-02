type HttpUrl = string;

type SocialsType = {
    linkedin?: HttpUrl;
}

type LaunchType = {
    title: string;
    link: string;
    description: string;
}

type FounderType = {
    name: string;
    bio: string;
    image: HttpUrl;
    company: string;
    company_url: HttpUrl;
    socials: SocialsType;
}

export type StartupType = {
    id?: string;
    scraped_url: HttpUrl;
    name: string;
    description: string;
    details: string;
    image: HttpUrl;
    website: HttpUrl;
    yc_batch: string;
    status: string;
    industries: string[];
    location?: string;
    founded: string;
    team_size: string;
    group_partner: string;
    founders: FounderType[];
    launches: LaunchType[];
}
