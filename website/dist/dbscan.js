var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
export function loadDBSCAN() {
    console.log("Loading DBSCAN content");
    function loadClusterPlot() {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                console.log('Loading cluster plot');
                //const response = await fetch('/src/assets/generated_plots/dbscan_clusters.html');
                //const plotHtml = await response.text();
                const content = document.getElementById('content');
                if (content) {
                    //console.log('innerHTML assigned to plotHtml');
                    content.innerHTML = `<iframe src="/src/assets/generated_plots/dbscan_clusters.html" style="width: 100%; height: 100%; border: none;"></iframe>`;
                }
                else {
                    console.error('Content element not found');
                }
            }
            catch (error) {
                console.error("Error loading the cluster plot:", error);
            }
        });
    }
    loadClusterPlot();
}
