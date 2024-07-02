import * as React from "react";
import { motion } from "framer-motion";
import { CardItem } from "./CardItem";
import { StartupType } from "../types";

interface SearchResultsProps {
    searchResults: StartupType[];
}

export const SearchResults: React.FC<SearchResultsProps> = ({ searchResults }) => {
    return (
        <motion.div
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-4"
            initial="hidden"
            animate="visible"
        >
            {searchResults.map((startup: StartupType, index: number) => (
                <CardItem startup={startup} key={startup.id} />
            ))}
        </motion.div>
    );
};
