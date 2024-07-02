"use client"
import { useState } from "react";
import { motion } from "framer-motion";
import { SearchComponent } from "./SearchComponent";
import { CoolSpline } from "./CoolSpline";
import { SearchResults } from "./SearchResults";
import { cn } from "@/lib/utils";
import { StartupType } from "../types";
import { LoadingResults } from "./LoadingResults";

export const SearchContainer = () => {
    const [searchResults, setSearchResults] = useState<StartupType[]>([]);
    const [loading, setLoading] = useState(false);

    const updateSearchResults = (results: any) => {
        setSearchResults(results);
    };

    const clearSearchResults = () => {
        setSearchResults([]);
    };

    const hasSearchResults = searchResults.length > 0;
    const hideGraphic = loading || hasSearchResults

    return (
        <div className={cn("w-full h-full flex flex-col items-center", hasSearchResults ? "justify-start" : "justify-center")} >
            {!hideGraphic && <h1 className="text-2xl font-bold">Find a startup</h1>}
            <motion.div
                className="flex flex-col gap-3 w-full items-center justify-center z-10"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.5, delay: 0.2 }}
            >
                <div className={cn("w-full px-2",
                    !(hideGraphic) ? "flex items-center justify-center" : "absolute top-0 backdrop-blur-md bg-white/10 py-2 shadow-sm z-30")}>
                    <SearchComponent
                        updateSearchResults={updateSearchResults}
                        clearSearchResults={clearSearchResults}
                        setLoading={setLoading}
                    />
                </div>
                {(hideGraphic) && (
                    <div className="absolute top-0 w-screen h-screen overflow-y-scroll flex-none pt-24 md:pt-14">
                        <div className="w-full h-full flex justify-center">
                            <div className="max-w-5xl" >
                                {loading ?
                                    <LoadingResults />
                                    :
                                    <SearchResults searchResults={searchResults} />
                                }
                            </div>
                        </div>
                    </div>
                )}
            </motion.div>
            {!hideGraphic && <CoolSpline />}
        </div>
    );
};