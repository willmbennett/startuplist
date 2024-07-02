import { motion } from "framer-motion";
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/app/components/ui/card";
export const LoadingResults = () => {
    const results = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    return (
        <motion.div
            className="w-full grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-4"
            initial="hidden"
            animate="visible"
            variants={{
                visible: { transition: { staggerChildren: 0.1 } }
            }}
        >
            {results.map((r, i) => (
                <motion.div key={i} className="animate-pulse">
                    <Card className="w-full h-96 flex flex-col justify-between p-4 shadow-md hover:shadow-lg transition-shadow duration-300">
                        <CardHeader>
                            <div className="flex items-center justify-between">
                                <div className="flex gap-2 justify-start items-center">
                                    <div className="w-12 h-12 aspect-square rounded-full border border-gray-200 shadow-sm overflow-hidden relative bg-gray-300">
                                        {/* Placeholder for image */}
                                    </div>
                                    <CardTitle className="text-xl font-semibold bg-gray-300 w-24 h-6 rounded-md"></CardTitle>
                                </div>
                                <div className="py-1 px-2 backdrop-blur-md bg-gray-300 rounded-lg w-16 h-6"></div>
                            </div>
                            <CardDescription className="text-sm text-gray-600 bg-gray-300 w-full h-4 rounded-md mt-2"></CardDescription>
                        </CardHeader>
                        <CardContent>
                            <div className="grid w-full items-center gap-4">
                                <div className="flex flex-col space-y-2">
                                    <div className="text-slate-600 bg-gray-300 w-full h-4 rounded-md"></div>
                                    <p className="bg-gray-300 w-16 h-4 rounded-md mt-2"></p>
                                    <div className="flex flex-wrap gap-2">
                                        <div className="py-1 px-2 backdrop-blur-md bg-gray-300 rounded-lg text-sm w-16 h-4"></div>
                                        <div className="py-1 px-2 backdrop-blur-md bg-gray-300 rounded-lg text-sm w-16 h-4"></div>
                                        <div className="py-1 px-2 backdrop-blur-md bg-gray-300 rounded-lg text-sm w-16 h-4"></div>
                                    </div>
                                    <p className="bg-gray-300 w-24 h-4 rounded-md mt-2"></p>
                                    <p className="bg-gray-300 w-20 h-4 rounded-md mt-2"></p>
                                </div>
                            </div>
                        </CardContent>
                        <CardFooter className="flex justify-center gap-2">
                            <div className="py-1 px-2 backdrop-blur-md bg-gray-300 rounded-lg w-12 h-6"></div>
                            <div className="py-1 px-2 rounded-lg bg-gray-300 w-12 h-6"></div>
                        </CardFooter>
                    </Card>
                </motion.div>
            ))}
        </motion.div>
    );
};
