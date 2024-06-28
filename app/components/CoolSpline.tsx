import Spline from "@splinetool/react-spline";
import { motion } from "framer-motion";

export const CoolSpline = ({ showSpline }: { showSpline: boolean }) => {
    return (
        <div className="w-full h-full absolute top-0 left-0 object-cover">
            <div className="w-full h-full flex items-center justify-center">
                <motion.div
                    className="w-full h-full flex items-center justify-center"
                    initial={{ opacity: 0.5, height: 0 }}
                    animate={{ opacity: showSpline ? 1 : 0.5, height: showSpline ? "100%" : 0 }}
                    transition={{ duration: 0.8 }}
                >
                    <Spline
                        style={{ width: '100%', height: '100%' }}
                        scene="https://prod.spline.design/LlnRnaq8w6PNLu0n/scene.splinecode"
                    />
                </motion.div>
            </div>
        </div>
    );
};