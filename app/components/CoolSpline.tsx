import Spline from "@splinetool/react-spline";

export const CoolSpline = () => {
    return (
        <div className="w-full h-full absolute top-0 left-0 object-cover">
            <div className="w-full h-full flex items-center justify-center">
                <Spline
                    style={{ width: '100%', height: '100%' }}
                    className=""
                    scene="https://prod.spline.design/LlnRnaq8w6PNLu0n/scene.splinecode"
                />
            </div>
        </div>
    );
};