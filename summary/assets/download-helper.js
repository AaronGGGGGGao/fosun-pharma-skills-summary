(function () {
  function triggerDownload(file) {
    const blob = new Blob([file.content], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = file.filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  window.attachSkillDownloads = function attachSkillDownloads(downloadableFiles) {
    document.querySelectorAll("[data-download-key]").forEach((button) => {
      button.addEventListener("click", () => {
        const file = downloadableFiles[button.dataset.downloadKey];
        if (file) {
          triggerDownload(file);
        }
      });
    });
  };
}());
