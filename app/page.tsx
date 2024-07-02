import { SearchContainer } from "./components/SearchContainer";

export default function Home() {
  return (
    <div className="h-screen w-screen overflow-hidden bg-gradient-to-tr from-black to-accent-900 text-white">
      <main className="flex flex-col w-full h-full items-center justify-center relative">
        <SearchContainer />
      </main>
    </div>
  );
}