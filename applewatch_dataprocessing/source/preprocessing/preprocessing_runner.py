import time

from source.analysis.figures.data_plot_builder import DataPlotBuilder
from source.analysis.setup.subject_builder import SubjectBuilder
from source.preprocessing.activity_count.activity_count_service import ActivityCountService
from source.preprocessing.feature_builder import FeatureBuilder
from source.preprocessing.raw_data_processor import RawDataProcessor
from source.preprocessing.time.circadian_service import CircadianService


def run_preprocessing(subject_set, crop=False):
    start_time = time.time()
    # we only need crop the data once
    if crop:
        for subject in subject_set:
            print("Cropping data from subject " + str(subject) + "...")
            RawDataProcessor.crop_all(str(subject))

    # ActivityCountService.build_activity_counts()  # This uses MATLAB, but has been replaced with a python implementation
    # CircadianService.build_circadian_model() # Both of the circadian lines require MATLAB to run
    # CircadianService.build_circadian_mesa()

    for subject in subject_set:
        FeatureBuilder.build(str(subject))

    end_time = time.time()
    print("Execution took " + str((end_time - start_time) / 60) + " minutes")


first_time_build = True
is_plot = False
subject_ids = SubjectBuilder.get_all_subject_ids()
run_preprocessing(subject_ids, crop=first_time_build)
if is_plot:
    for subject in subject_ids:
        DataPlotBuilder.make_data_demo(subject, False)
