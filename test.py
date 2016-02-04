import HeroAnalyser
import HeroAnalysisExporter

replay_path = r'C:\heroes\replays\ben\zag2.StormReplay'

analyser = HeroAnalyser.HeroAnalyser(replay_path)
analyser.analyze()
print HeroAnalysisExporter.analysis_string(analyser)
