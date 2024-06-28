"use client"
import { useState } from "react";
import { motion } from "framer-motion";
import { SearchComponent } from "./SearchComponent";
import { CoolSpline } from "./CoolSpline";
import { SearchResults } from "./SearchResults";
import { cn } from "@/lib/utils";
import { StartupType } from "../types";

export const SearchContainer = () => {
    const [searchResults, setSearchResults] = useState<StartupType[]>([]);

    const updateSearchResults = (results: any) => {
        console.log('about to update results with ', results);
        setSearchResults(results);
    };

    const clearSearchResults = () => {
        setSearchResults([]);
    };

    const hasSearchResults = searchResults.length > 0;

    return (
        <>
            <motion.div
                className={cn("z-10 w-full h-full flex flex-col items-center", hasSearchResults ? "justify-start" : "justify-center")}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
            >
                <h1 className="text-2xl font-bold">Find a startup</h1>
                <motion.div
                    className="flex flex-col gap-3 w-full items-center justify-center"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.5, delay: 0.2 }}
                >
                    <SearchComponent updateSearchResults={updateSearchResults} clearSearchResults={clearSearchResults} />
                    {hasSearchResults && (
                        <motion.div
                            className="max-w-5xl"
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5 }}
                        >
                            <SearchResults searchResults={searchResults} />
                        </motion.div>
                    )}
                </motion.div>
            </motion.div>
            <CoolSpline showSpline={!hasSearchResults} />
        </>
    );
};