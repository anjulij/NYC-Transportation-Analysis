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
                const response = yield fetch('/src/cluster_plot.html'); // Adjust the path if necessary
                const plotHtml = yield response.text();
                const content = document.getElementById('content');
                if (content) {
                    content.innerHTML = plotHtml;
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
