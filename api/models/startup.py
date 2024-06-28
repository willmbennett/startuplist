from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]

class SocialsModel(BaseModel):
    linkedin: Optional[HttpUrl] = None
    
class LaunchModel(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    description: str = Field(...)

class FounderModel(BaseModel):
    name: str = Field(...)
    bio: str = Field(...)
    image: HttpUrl = Field(...)
    company: str = Field(...)
    company_url: str = Field(...)
    socials: SocialsModel = Field(...)

class StartupModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    description: str = Field(...)
    details: List[str] = Field(...)
    image: HttpUrl = Field(...)
    website: HttpUrl = Field(...)
    yc_batch: str = Field(...)
    status: str = Field(...)
    industries: List[str] = Field(...)
    location: Optional[str] = None
    founded: str = Field(...)
    team_size: str = Field(...)
    group_partner: str = Field(...)
    founders: List[FounderModel] = Field(...)
    launches: List[LaunchModel] = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
"name": "Freestyle",
"description": "TLDR; You can use TypeScript for EVERYTHING\nFreestyle is a fundamental shift in how we approach web development. With Freestyle, you write your entire application—frontend and backend—in TypeScript. No context switching. No mental gymnastics. Just pure, consistent TypeScript throughout.\n\nRight now, building an application has a ton of disjointed layers. Imagine you’re writing a book in English for English readers. Now, imagine being told that all the connecting words—the “ands,” “buts,” and “ors”—must be written in Latin. Sounds absurd, right? Yet, this is often what web development feels like: you write your frontend in one language, only to switch to another for the backend, another for your database, and yet another to let your app connect to others.\n\nDuring our work for Apple, we lost hundreds of hours trying to integrate different layers and teams together to make our application run. That time should’ve been spent on features, but instead was spent on stitching features together. We created Freestyle not as a new stitching tool but as a way for whole organizations to not need those tools and instead function as a single unit.\nWhen you use Freestyle, you write your frontend and backend in JavaScript. Then, when you wanna call functions from your backend on your frontend, you just use them — no more dealing with REST APIs. When you want to store data, you just mark your JavaScript as @cloudstate and when you’re ready to deploy, you run npx freestyle deploy — and in one command you’re up and running.\nNo more SQL, no MongoDB, no Firebase, no GraphQL or REST, or anything else taking time away from building features. With Freestyle, all you need is TypeScript.\nReady to try it? Sign up for a demo here, or CHECK OUT THE DOCS HERE",
"details": [
"We build a new JavaScript Runtime + Framework that lets you write stateful JavaScript code without a database, and move data between application layers effortlessly. We empower your JavaScript Applications Engineers to move faster, collaborate better, and not need a database anymore."
],
"image": "https://bookface-images.s3.amazonaws.com/logos/1a1a193d6631b9ef5d237fb421e67a0345fb70b8.png",
"website": "https://www.freestyle.sh",
"yc_batch": "S24",
"status": "Active",
"industries": [
"developer-tools",
"web-development",
"cloud-computing"
],
"location": "San Francisco",
"founded": "2024",
"team_size": "5",
"group_partner": "Diana Hu",
"founders": [
{
"name": "Freestyle",
"bio": "Left UChicago to go to Apple, left Apple to found Freestyle.",
"image": "https://bookface-images.s3.amazonaws.com/avatars/e30e2f838d944c10ebb16771cd61490f10720dcf.jpg",
"company": "Freestyle",
"company_url": "/companies/freestyle",
"socials": {
"linkedin": "https://www.linkedin.com/in/benswerdlow/"
}
},
{
"name": "Freestyle",
"bio": "Jacob left college to go work as a contractor for Apple. After 16 months, he left to found Freestyle.",
"image": "https://bookface-images.s3.amazonaws.com/avatars/0f9d84a992c14cd10ee4b007d09c0d93df4b8491.jpg",
"company": "Freestyle",
"company_url": "/companies/freestyle",
"socials": {
"linkedin": "https://www.linkedin.com/in/jacobzwang/"
}
}
],
"launches": [
{
"title": "Freestyle: TypeScript for EVERYTHING",
"link": "/launches/LGW-freestyle-typescript-for-everything",
"description": "TLDR; You can use TypeScript for EVERYTHING\nFreestyle is a fundamental shift in how we approach web development. With Freestyle, you write your entire application—frontend and backend—in TypeScript. No context switching. No mental gymnastics. Just pure, consistent TypeScript throughout.\n\nRight now, building an application has a ton of disjointed layers. Imagine you’re writing a book in English for English readers. Now, imagine being told that all the connecting words—the “ands,” “buts,” and “ors”—must be written in Latin. Sounds absurd, right? Yet, this is often what web development feels like: you write your frontend in one language, only to switch to another for the backend, another for your database, and yet another to let your app connect to others.\n\nDuring our work for Apple, we lost hundreds of hours trying to integrate different layers and teams together to make our application run. That time should’ve been spent on features, but instead was spent on stitching features together. We created Freestyle not as a new stitching tool but as a way for whole organizations to not need those tools and instead function as a single unit.\nWhen you use Freestyle, you write your frontend and backend in JavaScript. Then, when you wanna call functions from your backend on your frontend, you just use them — no more dealing with REST APIs. When you want to store data, you just mark your JavaScript as @cloudstate and when you’re ready to deploy, you run npx freestyle deploy — and in one command you’re up and running.\nNo more SQL, no MongoDB, no Firebase, no GraphQL or REST, or anything else taking time away from building features. With Freestyle, all you need is TypeScript.\nReady to try it? Sign up for a demo here, or CHECK OUT THE DOCS HERE"
}
]
}
        },
    )

class UpdateStartupModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    details: Optional[List[str]] = None
    image: Optional[HttpUrl] = None
    website: Optional[HttpUrl] = None
    yc_batch: Optional[str] = None
    status: Optional[str] = None
    industries: Optional[List[str]] = None
    location: Optional[str] = None
    founded: Optional[str] = None
    team_size: Optional[str] = None
    group_partner: Optional[str] = None
    founders: Optional[List[FounderModel]] = None
    launches: Optional[List[str]] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
"name": "Freestyle",
"description": "TLDR; You can use TypeScript for EVERYTHING\nFreestyle is a fundamental shift in how we approach web development. With Freestyle, you write your entire application—frontend and backend—in TypeScript. No context switching. No mental gymnastics. Just pure, consistent TypeScript throughout.\n\nRight now, building an application has a ton of disjointed layers. Imagine you’re writing a book in English for English readers. Now, imagine being told that all the connecting words—the “ands,” “buts,” and “ors”—must be written in Latin. Sounds absurd, right? Yet, this is often what web development feels like: you write your frontend in one language, only to switch to another for the backend, another for your database, and yet another to let your app connect to others.\n\nDuring our work for Apple, we lost hundreds of hours trying to integrate different layers and teams together to make our application run. That time should’ve been spent on features, but instead was spent on stitching features together. We created Freestyle not as a new stitching tool but as a way for whole organizations to not need those tools and instead function as a single unit.\nWhen you use Freestyle, you write your frontend and backend in JavaScript. Then, when you wanna call functions from your backend on your frontend, you just use them — no more dealing with REST APIs. When you want to store data, you just mark your JavaScript as @cloudstate and when you’re ready to deploy, you run npx freestyle deploy — and in one command you’re up and running.\nNo more SQL, no MongoDB, no Firebase, no GraphQL or REST, or anything else taking time away from building features. With Freestyle, all you need is TypeScript.\nReady to try it? Sign up for a demo here, or CHECK OUT THE DOCS HERE",
"details": [
"We build a new JavaScript Runtime + Framework that lets you write stateful JavaScript code without a database, and move data between application layers effortlessly. We empower your JavaScript Applications Engineers to move faster, collaborate better, and not need a database anymore."
],
"image": "https://bookface-images.s3.amazonaws.com/logos/1a1a193d6631b9ef5d237fb421e67a0345fb70b8.png",
"website": "https://www.freestyle.sh",
"yc_batch": "S24",
"status": "Active",
"industries": [
"developer-tools",
"web-development",
"cloud-computing"
],
"location": "San Francisco",
"founded": "2024",
"team_size": "5",
"group_partner": "Diana Hu",
"founders": [
{
"name": "Freestyle",
"bio": "Left UChicago to go to Apple, left Apple to found Freestyle.",
"image": "https://bookface-images.s3.amazonaws.com/avatars/e30e2f838d944c10ebb16771cd61490f10720dcf.jpg",
"company": "Freestyle",
"company_url": "/companies/freestyle",
"socials": {
"linkedin": "https://www.linkedin.com/in/benswerdlow/"
}
},
{
"name": "Freestyle",
"bio": "Jacob left college to go work as a contractor for Apple. After 16 months, he left to found Freestyle.",
"image": "https://bookface-images.s3.amazonaws.com/avatars/0f9d84a992c14cd10ee4b007d09c0d93df4b8491.jpg",
"company": "Freestyle",
"company_url": "/companies/freestyle",
"socials": {
"linkedin": "https://www.linkedin.com/in/jacobzwang/"
}
}
],
"launches": [
{
"title": "Freestyle: TypeScript for EVERYTHING",
"link": "/launches/LGW-freestyle-typescript-for-everything",
"description": "TLDR; You can use TypeScript for EVERYTHING\nFreestyle is a fundamental shift in how we approach web development. With Freestyle, you write your entire application—frontend and backend—in TypeScript. No context switching. No mental gymnastics. Just pure, consistent TypeScript throughout.\n\nRight now, building an application has a ton of disjointed layers. Imagine you’re writing a book in English for English readers. Now, imagine being told that all the connecting words—the “ands,” “buts,” and “ors”—must be written in Latin. Sounds absurd, right? Yet, this is often what web development feels like: you write your frontend in one language, only to switch to another for the backend, another for your database, and yet another to let your app connect to others.\n\nDuring our work for Apple, we lost hundreds of hours trying to integrate different layers and teams together to make our application run. That time should’ve been spent on features, but instead was spent on stitching features together. We created Freestyle not as a new stitching tool but as a way for whole organizations to not need those tools and instead function as a single unit.\nWhen you use Freestyle, you write your frontend and backend in JavaScript. Then, when you wanna call functions from your backend on your frontend, you just use them — no more dealing with REST APIs. When you want to store data, you just mark your JavaScript as @cloudstate and when you’re ready to deploy, you run npx freestyle deploy — and in one command you’re up and running.\nNo more SQL, no MongoDB, no Firebase, no GraphQL or REST, or anything else taking time away from building features. With Freestyle, all you need is TypeScript.\nReady to try it? Sign up for a demo here, or CHECK OUT THE DOCS HERE"
}
]
}
        },
    )

class StartupCollection(BaseModel):
    startups: List[StartupModel]

# FastAPI setup and routes would be added here to interact with the MongoDB collection using the above models.