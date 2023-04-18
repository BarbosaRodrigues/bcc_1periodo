import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { ArtistEntity } from "./entities/artist.entity";
import { GenreEntity } from "./entities/genre.entity";
import { MovieEntity } from "./entities/movie.module";
import { MovieController } from "./movie.controller";
import { MovieService } from "./movie.service";

@Module({
    imports:[
        TypeOrmModule.forFeature([
            MovieEntity,
            ArtistEntity,
            GenreEntity,
    ]),
    ],
    providers: [MovieService],
    controllers: [MovieController],
    exports: [TypeOrmModule]
})
export class MovieModule{}