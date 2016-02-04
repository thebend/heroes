import HeroAnalysis
import HeroAnalysisExporter

replay_path = r'C:\heroes\replays\ben\zag2.StormReplay'

analysis = HeroAnalysis.analyze(replay_path)
print HeroAnalysisExporter.analysis_string(analysis)
