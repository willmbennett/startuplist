import * as React from "react";
import { motion } from "framer-motion";
import { CardItem } from "./CardItem";
import { StartupType } from "../types";

interface SearchResultsProps {
    searchResults: StartupType[];
}

const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 }
};

export const SearchResults: React.FC<SearchResultsProps> = ({ searchResults }) => {
    return (
        <motion.div
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-4"
            initial="hidden"
            animate="visible"
            variants={{
                visible: { transition: { staggerChildren: 0.1 } }
            }}
        >
            {searchResults.map((startup: StartupType, index: number) => (
                <motion.div key={index} variants={itemVariants}>
                    <CardItem startup={startup} />
                </motion.div>
            ))}
        </motion.div>
    );
};
