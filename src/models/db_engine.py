from sqlalchemy import create_engine


class Alchemy_engine:

    def create_engine():
        engine = create_engine(
            'postgresql://moneylover-data-analysis-bd_owner:5YRXbJmf3vxG@ep-spring-night-a5cjpiw1.us-east-2.aws.neon.tech/moneylover-data-analysis-bd', echo=True)
        return engine
