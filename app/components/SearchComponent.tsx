"use client"
import { Input } from "@/app/components/ui/input";
import { Search } from "lucide-react";
import { X } from "lucide-react";
import { useState, useEffect, Dispatch, SetStateAction } from "react";
import { motion } from "framer-motion";
import { fetchEmbeddings } from "@/lib/openai";
import { Button } from "./ui/button";
import { StartupType } from "../types";

const placeholders = ["Non AI startups from YCS24 batch", "Fintch startups in New York", "Data integration startups", "Green energy startups"];

interface SearchComponentProps {
    updateSearchResults: (results: StartupType[]) => void;
    clearSearchResults: () => void;
    setLoading: Dispatch<SetStateAction<boolean>>
}

export const SearchComponent = ({ updateSearchResults, clearSearchResults, setLoading }: SearchComponentProps) => {
    const [searchValue, setSearchValue] = useState("");
    const [placeholder, setPlaceholder] = useState(placeholders[0]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [showPlaceholder, setShowPlaceholder] = useState(true);

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentIndex((prevIndex) => (prevIndex + 1) % placeholders.length);
            setShowPlaceholder(false); // Hide the current placeholder before switching
        }, 3000); // Change every 3 seconds

        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        if (!showPlaceholder) {
            setPlaceholder(placeholders[currentIndex]);
            setShowPlaceholder(true);
        }
    }, [currentIndex, showPlaceholder]);

    const typingVariants = {
        hidden: { opacity: 0 },
        visible: (i: any) => ({
            opacity: 1,
            transition: {
                delay: i * 0.05
            }
        })
    };

    const handleSearch = async () => {
        setLoading(true)
        const data = await fetchEmbeddings(searchValue)
        updateSearchResults(data.startups)
        setLoading(false)
    };

    const handleClear = () => {
        clearSearchResults()
        setSearchValue("")
    }

    return (
        <div className="flex flex-col md:flex-row justify-center items-center gap-2 w-full">
            <div className="relative flex-1 md:grow-0 w-full">
                <Search className="absolute left-3 top-3 h-4 w-4 text-white" />
                <Input
                    type="search"
                    placeholder=""
                    value={searchValue}
                    onChange={(e) => setSearchValue(e.target.value)}
                    className="w-full pl-10 md:w-[200px] lg:w-[336px]"
                />
                {!searchValue && showPlaceholder && (
                    <div className="absolute left-10 top-2 w-full h-full text-white pointer-events-none text-white flex">
                        {placeholder.split("").map((char, index) => (
                            <motion.span
                                key={index}
                                custom={index}
                                initial="hidden"
                                animate="visible"
                                variants={typingVariants}
                                style={{ whiteSpace: 'pre' }} // Ensure spaces are preserved
                            >
                                {char}
                            </motion.span>
                        ))}
                    </div>
                )}
                {searchValue && (
                    <button
                        className="absolute right-3 top-3 h-4 w-4 text-white z-30"
                        onClick={handleClear}
                    >
                        <X className="h-4 w-4" />
                    </button>
                )}
            </div>
            <Button
                size="md"
                variant="ghost"
                className="w-full md:w-auto"
                disabled={!searchValue}
                onClick={handleSearch}
            >
                Search
            </Button>
        </div>
    );
};