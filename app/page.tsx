import Spline from "@splinetool/react-spline";
import { SearchComponent } from "./components/SearchComponent";

export default function Home() {
  return (
    <div className="h-screen w-screen overflow-hidden bg-gradient-to-tr from-black to-accent-900 text-white">
      <main className="flex flex-col w-full h-full items-center justify-center relative">
        <div className="z-10 w-full flex flex-col items-center justify-center px-3">
          <h1 className="text-2xl font-bold">Find a startup</h1>
          <div className="flex w-full items-center justify-center">
            <SearchComponent />
          </div>
        </div>
        <div className="w-full h-full absolute top-0 left-0 object-cover">
          <Spline
            style={{ width: '100%', height: '100%' }}
            scene="https://prod.spline.design/LlnRnaq8w6PNLu0n/scene.splinecode"
          />
        </div>
      </main>
    </div>
  );
}